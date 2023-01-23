from django.shortcuts import render
from django.http import HttpResponse
from .models import place, destination


# Create your views here.
# def fun(request):
#     return HttpResponse("HELLO WORLD")


def fun(request):
    obj = place.objects.all()
    dest = destination.objects.all()
    return render(request, "index.html", {'results': obj, 'destination': dest})


def about(request):
    dest = destination.objects.all()
    return render(request, "about.html",  {'destination': dest})


def contact(request):
    dest = destination.objects.all()
    return render(request, "contact.html",  {'destination': dest})


def services(request):
    dest = destination.objects.all()
    return render(request, "service.html",  {'destination': dest})


def package(requist):
    dest = destination.objects.all()
    return render(requist, 'package.html',  {'destination': dest})


def trip(requist):
    return render(requist, 'trip.html')
