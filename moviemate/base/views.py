# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
import json
from .models import *
from django.utils import timezone
from django.contrib.auth.decorators import user_passes_test
from django.utils.safestring import mark_safe

from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')

def signup_user(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        try:
            print("TRY")
            User.objects.create_user(username=username, password=password, email=email)
        except Exception as e:
            print("EXCEPTIOn")
            context={'errormsg': "1"}
            render(request, 'signup.html', context)
        else:
            print("ELSE")
            # Redirect to the desired page after successful signup
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to the desired page after login
                return redirect('home')


    return render(request, 'signup.html', context)


def login_user(request):
     
    if request.user.is_authenticated:
        return redirect('order')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to the distributor's dashboard or desired page after login
            return redirect('home')

    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('home')