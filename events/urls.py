from django.urls import path
from . import views

urlpatterns = [
    path('event_detail', views.event_detail, name='event_detail'),
    path('event_list', views.event_list, name='event_list'),
    path('new_event_request', views.new_event_request, name='new_event_request'),

]
