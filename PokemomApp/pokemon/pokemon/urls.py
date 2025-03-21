from django.urls import path
from .views import DashboardView 
from .views import PesoView
from .views import PokemonGrass
from .views import PokemonFlying
from . import views


urlpatterns = [
    #pokemons 
    path('', views.index, name="index"), 
    #dashboard/amount/
    #path("<int:amount>/", views.dashboard, name="dashboard"),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('peso/', PesoView.as_view(), name='peso'),
    path('tipoGrass/', PokemonGrass.as_view(), name= 'tipoGrass'),
    path('voladores/', PokemonFlying.as_view(), name= 'voladores')
]