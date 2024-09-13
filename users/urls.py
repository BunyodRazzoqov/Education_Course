from django.contrib import admin
from django.urls import path

from users import views

urlpatterns = [
    path('sending-email/', views.SendEmailView.as_view(), name='send_email'),
    path('success/', views.success, name='success'),
    path('login/', views.LoginPageView.as_view(), name='login_page'),
    path('register/', views.register_page, name='register_page'),
    path('activation-link/<uidb64>/<token>/', views.activate, name='activate'),
]
