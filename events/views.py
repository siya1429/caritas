from django.shortcuts import render

# Create your views here.
def detail(request, id):
  return render(request, 'events/detail.html')

def list(request):
  return render(request, 'events/list.html')

def new(request):
  return render(request, 'events/new.html')