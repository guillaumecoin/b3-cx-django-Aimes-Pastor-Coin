# Generated by Django 4.1.7 on 2023-03-08 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appResa', '0003_reservation_nom_ecole'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='nom_ecole',
            field=models.CharField(default='ecole1', max_length=100),
        ),
    ]