from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import redirect


"""Testing"""

def home(request):
    count = User.objects.count()

    return render(request, 'home.html', {
        'count': count
    })

def signupTest(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })

"""End Testing"""

def index(request):
    return render(request, "MideTuRiesgo/mideturiesgo.html")

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/MideTuRiesgo/encuesta')
    else:
        form = UserCreationForm()
    return render(request, "registration/registrarse.html", {
        'form': form
    })


def dos(request):
    return render(request, "MideTuRiesgo/mideturiesgo2.html")

def profile(request):
    return render(request, "registration/profile.html")


