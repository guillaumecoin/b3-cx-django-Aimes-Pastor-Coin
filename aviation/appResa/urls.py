from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.login_vue, name='login'),
    path('accueil/', views.accueil, name='accueil'),
    path('mes_reservations/', views.mes_reservations, name='mes_reservations'),
    path('reserver/', views.reserver, name='reserver')
    # path('reserver/<int:ecole_id>', views.reserver, name='reserver')
]