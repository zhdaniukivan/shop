from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Pizza, Soup, Feedback, Bascet
from django.http import HttpResponse, HttpResponseRedirect
from .forms import FeedbackForm, AddInBascetForm


# Create your views here.


# def home(request):
#     return render(request, 'pizzashopapp/home.html')

#
# def pizzashopapp_home(request):
#     return render(request, 'pizzashopapp/home.html', {})
#
# def pizzashopapp_sign_up(requst):
#     return render(requst, 'pizzashopapp/sign_sign_up.html', {})


def pizzashopapp_all(request):
    pizzas = Pizza.objects.all()
    soups = Soup.objects.all()

    if request.method == 'POST':
        form = AddInBascetForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            for pizza in pizzas:
                feed = Bascet(
                    name=pizza.name,
                    amount=form.cleaned_data['amount'],
                )
                feed.save()
    else:
        form = AddInBascetForm()

    return render(request, 'pizzashopapp/home.html', {'pizzas': pizzas, 'soups': soups, 'form': form})
def bascket(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            feed = Feedback(
                name=form.cleaned_data['name'],
                surname=form.cleaned_data['surname'],
                feedback=form.cleaned_data['feedback'],
                rating=form.cleaned_data['rating'],
            )
            feed.save()
            return HttpResponseRedirect('/done')
    else:
        form = FeedbackForm()
    return render(request, 'pizzashopapp/bascket.html', {'form': form})

def done(request):
    return render(request, 'pizzashopapp/done.html', {})