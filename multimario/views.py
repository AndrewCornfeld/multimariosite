from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import render, redirect


def home(request):
    return render(request, 'multimario/home.html')


def logout_view(request):
    logout(request)
    return redirect("/")


def upcomingraces(request):
    return render(request, 'multimario/upcomingraces.html')


def glossary(request):
    return render(request, 'multimario/glossary.html')

# def create(response):
# return render(response, 'multimario/create.html')

# Create your views here.
