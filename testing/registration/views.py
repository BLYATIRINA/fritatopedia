from django.shortcuts import render
from .models import *
from django.contrib.auth import get_user_model

from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):
    return render(request, 'registration/registration.html')



def profile_view(request):
    ser = get_user_model()
    users = ser.objects.all()
    d = {'users': users}
    return render(request, 'registration/profile.html', d)


def login(request):
    return render(request, 'registration/login.html')
