from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from .models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
def login_view(request):
  if request.method == 'POST':
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(email=email, password=password)

    if user is not None:
      login(request, user)
      return redirect('index')
  return render(request, 'users/login.html')

def logout_view(request):
  logout(request)
  return render(request, 'users/logout.html')

@login_required(login_url='login')
def password_reset(request):
  return render(request, 'users/password_reset.html')

@login_required(login_url='login')
def profile(request):
  user = request.user
  context = {
    'user':user
  }
  return render(request, 'users/profile.html', context)

def register(request):
  if request.method == 'POST':
    full_name = request.POST.get('full_name')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    password = request.POST.get('password')
    
    user = User(full_name=full_name, phone=phone, email=email)
    user.set_password(password)
    user.save()
    return redirect('login')
  return render(request, 'users/register.html')