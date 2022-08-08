from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='event_list'),
    path('<int:id>/detail/', views.detail, name='event_detail'),
    path('new/', views.new, name='event_request_new'),

]
