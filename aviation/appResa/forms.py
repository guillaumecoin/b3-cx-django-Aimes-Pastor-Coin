from django import forms
from .models import Reservation
# from django.contrib.auth.forms import AuthenticationForm

class ReservationForm(forms.ModelForm):
    
    class Meta:
        model = Reservation
        fields = ['nom', 'date_arrivee', 'date_depart', 'nombre_personnes']

class LoginForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur")
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)