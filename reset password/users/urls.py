from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.CreateUser.as_view(), name='signup'),
    path('signin/', views.SignIn.as_view(), name='signin'),
    path('send-otp/', views.SendOTP.as_view(), name='send-otp'),
    path('verify-otp/', views.VerifyOTP.as_view(), name='verify-otp'),
    path('reset-password/', views.ResetPassword.as_view(), name='reset-password'),
]