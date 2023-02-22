from django.shortcuts import render
from .forms import ReservationForm
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
#Requete du formulaire

def reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'reservation_confirm.html')
        else:
            form = ReservationForm()
        return render(request, 'appResa/reservation.html', {'form': form})

def index(request):
    return HttpResponse("Hello World !")


def login(request):
    form = AuthenticationForm()
    return render(request, 'appResa/login.html', {'form': form})