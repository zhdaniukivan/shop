from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Pizza, Soup
from django.http import HttpResponse
# Create your views here.

def home(request):
    return redirect(pizzashopapp_home)

@login_required(login_url='/pizzashopapp/sign-in')
def pizzashopapp_home(request):
    return render(request, 'pizzashopapp/home.html', {})

def pizzashopapp_sign_up(requst):
    return render(requst, 'pizzashopapp/sign_sign_up.html', {})


def pizzashopapp_all(request):
    pizzas = Pizza.objects.all()
    soups = Soup.objects.all()
    return render(request, 'pizzashopapp/home.html', {'pizzas':pizzas, 'soups':soups})

