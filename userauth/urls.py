from django.urls import path
from .views import RegisterView, LoginView, HomeView, HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name = "home"),
    path("register/", RegisterView.as_view(), name = 'register'),
    path("login/", LoginView.as_view(), name = 'login'),
    path("home/", HomeView.as_view(), name = 'home')
    
]
