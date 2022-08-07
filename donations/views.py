from django.shortcuts import render

# Create your views here.
def previous_donations_list(request):
  return render(request, 'donations/previous_donations_list.html')

def new_donation(request):
  return render(request, 'donations/new_donation.html')

def donation_payment_id(request):
  return render(request, 'donations/donation_payment_id.html')

def donation_detail(request):
  return render(request, 'donations/donation_detail.html')
