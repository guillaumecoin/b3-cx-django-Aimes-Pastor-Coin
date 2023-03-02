from django.db import models

class Reservation(models.Model):
    nom = models.CharField(max_length=100)
    date_arrivee = models.DateField()
    date_depart = models.DateField()
    nombre_personnes = models.IntegerField()
    
    def __str__(self):
        return self.nom

class Ecole(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=200)
    ville = models.CharField(max_length=100)
    description = models.TextField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nom