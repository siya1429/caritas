from django.contrib import messages
from django.shortcuts import render
from .models import Contact
# Create your views here.
def index(request):
  return render(request, 'home/index.html')

def contact_us(request):
  if request.method == 'POST':
    name = request.POST.get('name')
    description = request.POST.get('description')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    contact = Contact(name=name, description=description, email=email, phone=phone)
    contact.save()
    messages.success(request, 'We have recieved your request.')
  return render(request, 'home/contact_us.html')


def about_us(request):
  return render(request, 'home/about_us.html')