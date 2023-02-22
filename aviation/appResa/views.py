from django.shortcuts import render
from .forms import ReservationForm
from django.http import HttpResponse

#Requete du formulaire

def reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'reservation_confirm.html')
        else:
            form = ReservationForm()
        return render(request, 'reservation.html', {'form': form})

def index(request):
    return HttpResponse("Hello World !")