from django.shortcuts import render

# Create your views here.
def login(request):
  return render(request, 'users/login.html')

def logout(request):
  return render(request, 'users/logout.html')

def password_reset(request):
  return render(request, 'users/password_reset.html')

def profile(request):
  return render(request, 'users/profile.html')

def register(request):
  return render(request, 'users/register.html')