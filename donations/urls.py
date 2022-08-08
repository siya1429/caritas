from tkinter import N
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='donation_list'),
    path('new/', views.new, name='donation_new'),
    path('donation_payment_id/', views.donation_payment_id, name='donation_payment_id'),
    path('<int:id>/detail/', views.detail, name='donation_detail')
]
