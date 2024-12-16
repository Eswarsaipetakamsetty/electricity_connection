from django.urls import path
from . import views



urlpatterns = [
    path('request/', views.requestConnection, name= 'request-connection'),
]
