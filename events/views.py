from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Event
# Create your views here.
def detail(request, id):
  return render(request, 'events/detail.html')

@login_required(login_url='login')
def list(request):
  if request.method == "POST":
    name = request.POST.get('name')
    event_list = Event(name=name)
    event_list.save()
    return redirect('event_list')
  return render(request, 'events/list.html')

@login_required(login_url='login')
def new(request):
  if request.method == "POST":
    name = request.POST.get('name')
    description = request.POST.get('description')
    purpose = request.POST.get('purpose')
    event_date = request.POST.get('event_date')
    user = request.user
    new_event = Event(name=name, description=description, purpose=purpose, event_date=event_date, user=user)
    new_event.save()
    return redirect('event_list')
  return render(request, 'events/new.html')