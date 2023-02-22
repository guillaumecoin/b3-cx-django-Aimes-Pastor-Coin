from django.db import models

class Reservation(models.Model):
    nom = models.CharField(max_length=100)
    date_arrivee = models.DateField()
    date_depart = models.DateField()
    nombre_personnes = models.IntegerField()
    
    def __str__(self):
        return self.nom

