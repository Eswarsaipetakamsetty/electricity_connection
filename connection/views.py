from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ElectricityConnectionForm
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, api_view



def requestConnection(request):
    if request.method == 'POST':
        form = ElectricityConnectionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'connection/success.html')
    else:
        form = ElectricityConnectionForm()
    return render(request, 'connection/request_form.html', {'form' : form})

