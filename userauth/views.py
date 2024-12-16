from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework.permissions import AllowAny
from django.views.generic import TemplateView

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return render(request, "userauth/register.html")

    def post(self, request):
        serializer = RegisterSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return render(request, "userauth/register.html",{"message" : "User Registered successsfully"})
        return render(request, "userauth/register.html",{"errors" : serializer.errors})

class LoginView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return render(request, "userauth/login.html")
    

    def post(self, request):
        serializer = LoginSerializer(data = request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username = username, password = password)
            print(f"User: {user}")
            if user:
                refresh = RefreshToken.for_user(user)
                request.session['access_token'] = str(refresh.access_token)
                request.session['refresh_token'] = str(refresh)
                return redirect('home')
            return render(request, "userauth/login.html",{
                "error" : "Invalid credentials"
            })
        return render(request, "userauth/login.html",{
                "error" : serializer.errors
            })
    
class HomeView(TemplateView):
    template_name = "userauth/home.html"


class HomePageView(TemplateView):
    template_name = "userauth/home_page.html"
    