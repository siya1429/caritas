from django.shortcuts import render

# Create your views here.
def list(request):
  return render(request, 'donations/list.html')

def new(request):
  return render(request, 'donations/new.html')

def donation_payment_id(request):
  return render(request, 'donations/donation_payment_id.html')

def detail(request, id):
  return render(request, 'donations/detail.html')
