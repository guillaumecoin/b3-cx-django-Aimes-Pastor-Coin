from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_protect
from .models import Ecole,Reservation
from .forms import LoginForm,ReservationForm
from django.views.decorators.http import require_POST

#Requete du formulaire



@require_POST
def supprimer_ecole(request, reservation_id):
    ecole = get_object_or_404(Reservation, pk=reservation_id)
    ecole.delete()
    return redirect('mes_reservations')

def index(request):
    return HttpResponse("Hello World !")

def reservationEcole(request, nom_ecole):
    reservations = Reservation.objects.filter(nom_ecole=nom_ecole)
    context = {'reservations': reservations}
    return render(request, 'appResa/reservationsEcole.html', context)

def login_vue(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        # initalisation du formulaire
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
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
    #recupere les ecole disponible
    # ecoles = Ecole.objects.filter(disponible=True)
    ecoles = Ecole.objects.all()
    username = None
    if request.user.is_authenticated:
        #verifie si l'user est authentifie
        username = request.user.username
    #faire passer toutes les infos dans context
    context = {'ecoles': ecoles,'username': username}
    return render(request, 'appResa/accueil.html', context)



def mes_reservations(request):
    reservations = Reservation.objects.filter(nom_client=request.user.username)
    context = {'reservations': reservations}
    return render(request, 'appResa/mes_reservations.html', context)

def mes_reservations(request):
    reservations = Reservation.objects.filter(nom_client=request.user.username)
    context = {'reservations': reservations}
    return render(request, 'appResa/mes_reservations.html', context)



def reserver(request):
    #recupérer l'ecole avec son id
    # ecole = get_object_or_404(Ecole, pk=ecole_id)
    if request.method == 'POST':
            nom_ecole = request.POST.get('nom_ecole')
            date_arrivee = request.POST.get('date_arrivee')
            date_depart = request.POST.get('date_depart')
            nom_client = request.POST.get('nom_client')
            nombre_personnes = request.POST.get('nombre_personnes')
            #si form valid enregistrer la reservation
            Reservation.objects.create(nom_client=nom_client,nom_ecole=nom_ecole,date_arrivee=date_arrivee,date_depart=date_depart, nombre_personnes=nombre_personnes)
            return HttpResponse("Ajouté")
            # return redirect('mes_reservations')
    else:
        return redirect('mes_reservations')