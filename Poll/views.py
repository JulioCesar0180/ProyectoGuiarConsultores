from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return render(request, "MideTuRiesgo/mideturiesgo.html")

def dos(request):
    return render(request, "MideTuRiesgo/mideturiesgo2.html")



