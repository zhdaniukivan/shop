from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Pizza, Soup
from django.http import HttpResponse, HttpResponseRedirect
from .forms import FeedbackForm


# Create your views here.


def home(request):
    return redirect('/home')

@login_required(login_url='/pizzashopapp/sign-in')
def pizzashopapp_home(request):
    return render(request, 'pizzashopapp/home.html', {})

def pizzashopapp_sign_up(requst):
    return render(requst, 'pizzashopapp/sign_sign_up.html', {})


def pizzashopapp_all(request):
    pizzas = Pizza.objects.all()
    soups = Soup.objects.all()
    return render(request, 'pizzashopapp/home.html', {'pizzas':pizzas, 'soups':soups})

def bascket(request):
    form = FeedbackForm()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect('done')
    form = FeedbackForm()
    return render(request, 'pizzashopapp/bascket.html', {'form':form})

def done(request):
    return render(request, 'pizzashopapp/done.html', {})