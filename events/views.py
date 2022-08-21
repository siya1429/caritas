from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Event
from django.contrib import messages


# Create your views here.

@login_required(login_url='login')
def detail(request, id):
  try:
    event = Event.objects.get(id=id, user=request.user)
    context = {
      'event' : event
    }
    return render(request, 'events/detail.html', context)
  except Event.DoesNotExist:
    messages.error(request, 'Event not found')
    return redirect('event_list')

@login_required(login_url='login')
def list(request):
    events = Event.objects.filter(user=request.user)
    context ={
      'events' : events
    }
    return render(request, 'events/list.html', context)

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