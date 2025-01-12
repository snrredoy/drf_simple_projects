from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from resetPassword import settings
from .models import OTP
from django.core.mail import send_mail
from django.contrib.auth.models import User
import random
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import UserSerializer
# Create your views here.
def generate_otp():
    return random.randint(100000, 999999)

def send_otp(email, otp):

    return send_mail(
        subject='OTP Verification',
        message=f'Your OTP is {otp} . Please do not share it with anyone. It is valid for 10 minutes.',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
    )


class CreateUser(APIView):

    permission_classes=[]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                'message': 'User created successfully',
                "data": serializer.data
            })
        return Response({
            "status": "error",
            'message': 'User creation failed',
            "data": serializer.errors
        })
    
class SignIn(APIView):

    permission_classes=[]

    def post(self, request):

        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        
        # if email is None or password is None:
        #     return Response({
        #         'status': 'error',
        #         'message': 'Please provide both email and password.',
        #         }, status=status.HTTP_400_BAD_REQUEST)
        if not username or not password:
            return Response({
                'status': 'error',
                'message': 'Username and password are required.'
            }, status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        print(user)
        
        if user is None:
            return Response({
                'status': 'error',
                'error': 'Invalid credentials.'
                }, status=status.HTTP_401_UNAUTHORIZED)
        
        refresh = RefreshToken.for_user(user)
        return Response({
            'status': 'success',
            'message': 'Login successful.',
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })


class SendOTP(APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        email = request.data.get('email')
        user = request.user
        otp = generate_otp()
        OTP.objects.update_or_create(user=user, defaults={'otp': otp})
        send_otp(email, otp)

        return Response({
            'status': 'success',
            'message': 'OTP sent successfully.'
        })
    
class VerifyOTP(APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        otp = request.data.get('otp')
        user = request.user

        try:
            otp_obj = OTP.objects.get(user=user)
        except OTP.DoesNotExist:
            return Response({
                'status': 'error',
                'message': 'OTP not found.'
            }, status=status.HTTP_400_BAD_REQUEST)

        if not otp_obj:
            return Response({
                'status': 'error',
                'message': 'OTP not found.'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        if otp_obj.attempt >= 3:
            otp_obj.delete()
            return Response({
                'status': 'error',
                'message': 'You have reached the maximum number of attempts. Please request a new OTP.'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        if not otp_obj.is_valid():
            otp_obj.delete()
            return Response({
                'status': 'error',
                'message': 'OTP has expired. Please request a new one.'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        if otp_obj.otp != otp:
            otp_obj.attempt += 1
            otp_obj.save()
            return Response({
                'status': 'error',
                'message': 'OTP does not match. Please try again.'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        otp_obj.is_varified = True
        otp_obj.save()

        return Response({
            'status': 'success',
            'message': 'OTP verified successfully.'
        })
    
class ResetPassword(APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        new_password = request.data.get('new_password')
        user = request.user

        try:
            otp_obj = OTP.objects.get(user=user)
        except OTP.DoesNotExist:
            return Response({
                'status': 'error',
                'message': 'OTP not found.Please verify your OTP first.'
            }, status=status.HTTP_400_BAD_REQUEST)

        if not otp_obj.is_varified:
            return Response({
                'status': 'error',
                'message': 'OTP not verified.Please verify your OTP before resetting your password.'
            }, status=status.HTTP_403_FORBIDDEN)

        user.set_password(new_password)
        user.save()

        otp_obj.delete()

        return Response({
            'status': 'success',
            'message': 'Password reset successfully.'
        })