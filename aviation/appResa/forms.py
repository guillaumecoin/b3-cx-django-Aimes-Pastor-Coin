from django import forms
from .models import Reservation

class QuestionForm(forms.ModelForm):
    
    class Meta:
        model = Reservation
        field = ['nom', 'date_arrivee', 'date_depart', 'nombre_personnes']