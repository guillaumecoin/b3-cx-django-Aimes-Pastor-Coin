from django import forms
from .models import Reservation


class LoginForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur")
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['nom_ecole', 'nom_client', 'date_arrivee', 'date_depart', 'nombre_personnes']
