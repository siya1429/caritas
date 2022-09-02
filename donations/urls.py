from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='donation_list'),
    path('new/', views.new, name='donation_new'),
    path('<int:id>/payment/', views.donation_payment, name='donation_payment'),
    path('<int:id>/detail/', views.detail, name='donation_detail')
]
