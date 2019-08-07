from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .forms import SignUpForm

"""Testing"""

def home(request):
    count = User.objects.count()

    return render(request, 'home.html', {
        'count': count
    })


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})



def index(request):
    return render(request, "MideTuRiesgo/mideturiesgo.html")


def dos(request):
    return render(request, "MideTuRiesgo/mideturiesgo2.html")

def profile(request):
    return render(request, "registration/profile.html")


