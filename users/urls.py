from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('password_reset/', views.password_reset, name='password_reset'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),


]
