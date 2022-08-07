from django.shortcuts import render

# Create your views here.
def event_detail(request):
  return render(request, 'events/event_detail.html')

def event_list(request):
  return render(request, 'events/event_list.html')

def new_event_request(request):
  return render(request, 'events/new_event_request.html')