from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, 'home/index.html')

def contact_us(request):
  return render(request, 'home/contact_us.html')


def about_us(request):
  return render(request, 'home/about_us.html')