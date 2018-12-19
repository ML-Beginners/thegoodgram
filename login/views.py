from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import NameForm

# Create your views here.


def login(request):

    return render(request, 'login/login.html')

def home(request):
    return render(request, 'login/home.html')

def register(request):
    return render(request, 'login/register.html')