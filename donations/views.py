from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Donation
from django.contrib import messages
import razorpay
from django.conf import settings
client = razorpay.Client(
    auth=(settings.RAZORPAY_KEY, settings.RAZORPAY_SECRET))

# Create your views here.


def list(request):
    return render(request, 'donations/list.html')


@login_required(login_url='login')
def new(request):
    if request.method == "POST":
        category = request.POST.get('category')
        amount = request.POST.get('amount')
        user = request.user
        donation = Donation(category=category, amount=amount, user=user)
        donation.save()
        return redirect('donation_payment', id=donation.id)
        print("messages donation saved")
    return render(request, 'donations/new.html')


@login_required(login_url='login')
def donation_payment(request, id):
    try:
        donation = Donation.objects.get(id=id, user=request.user)
        data = {
            'amount': int(donation.amount) * 100,
            'currency': 'INR',
            'receipt': 'order_'
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


def detail(request, id):
    return render(request, 'donations/detail.html')
