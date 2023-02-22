from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    
    class Meta:
        model = Reservation
        fields = ['nom', 'date_arrivee', 'date_depart', 'nombre_personnes']