from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from .forms import ReservationForm
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .models import Ecole
from .forms import LoginForm
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


def login_vue(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        # initalisation du formulaire
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            #verification des mots de passe et identifiant
            if user is not None:
                login(request, user)
                #enregistre l'utilisateur
                return redirect('accueil')
            else:
                form.add_error(None, 'incorrect')
    else:
        form = LoginForm()
    return render(request, 'appResa/login.html', {'form': form})

def accueil(request):
    ecoles = Ecole.objects.filter(disponible=True)
    username = None
    if request.user.is_authenticated:
        #verifie si l'user est authentifie
        username = request.user.username
    #faire passer toutes les infos dans context
    context = {'ecoles': ecoles,'username': username}
    return render(request, 'appResa/accueil.html', context)

def redirectVuePerso(request):
    return redirect('reservationP')

def reservationP(request):
    return HttpResponse("Hello reserve!")