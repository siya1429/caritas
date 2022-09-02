import uuid
import razorpay
from razorpay.errors import SignatureVerificationError
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.conf import settings
from .models import Donation

client = razorpay.Client(auth=(settings.RAZORPAY_ID, settings.RAZORPAY_SECRET))

def list(request):
    return render(request, 'donations/list.html')


@login_required(login_url='login')
def new(request):
    if request.method == "POST":
        category = request.POST.get('category')
        amount = request.POST.get('amount')
        user = request.user
        transaction_id = uuid.uuid4().hex
        donation = Donation(category=category, amount=amount, user=user, transaction_id=transaction_id)
        donation.save()
        
        return redirect('donation_payment', id=donation.id)
    return render(request, 'donations/new.html')


@login_required(login_url='login')
def donation_payment(request, id):
    try:
        donation = Donation.objects.get(id=id, user=request.user)
        data = {
            'amount': float(donation.amount) * 100,
            'currency': 'INR',
            # receipt_2
            'receipt': 'receipt_{}'.format(donation.id)
        }
        payment = client.order.create(data=data)
        context = {
            'payment': payment,
            'donation': donation,
            'razorpay_id': 'rzp_test_2xNEbcfBOh8cWh'
        }
        return render(request, 'donations/donation_payment.html', context)
    except Donation.DoesNotExist:
        messages.error(request, 'Error while finding donation')
        return redirect('donation_list')


@login_required(login_url='login')
@csrf_exempt
def payment_status(request, id):
    if request.method == 'POST':
        razorpay_payment_id = request.POST.get('razorpay_payment_id')
        razorpay_order_id = request.POST.get('razorpay_order_id')
        razorpay_signature = request.POST.get('razorpay_signature')

        try:
            client.utility.verify_payment_signature({
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': razorpay_payment_id,
                'razorpay_signature': razorpay_signature
            })

            try:
                donation = Donation.objects.get(id=id, user=request.user)
                donation.status = 'PAID'
                donation.payment_id = razorpay_payment_id
                donation.save()

                return render(request, 'donations/payment_status.html')
            except Donation.DoesNotExist:
                messages.error(request, 'Donation not found')
                return redirect('donation_list')
        except SignatureVerificationError:
            messages.error(request, 'Payment Verification Failed!')
            return redirect('donation_detail', id=id)    


def detail(request, id):
    return render(request, 'donations/detail.html')
