from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.login_vue, name='login'),
    path('accueil/', views.accueil, name='accueil'),
]