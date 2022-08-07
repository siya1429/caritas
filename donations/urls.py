from tkinter import N
from django.urls import path
from . import views

urlpatterns = [
    path('previous_donations_list/', views.previous_donations_list, name='previous_donations_list'),
    path('new_donation', views.new_donation, name='new_donation'),
    path('donation_payment_id', views.donation_payment_id, name='donation_payment_id'),
    path('donation_detail', views.donation_detail, name='donation_detail')
]
