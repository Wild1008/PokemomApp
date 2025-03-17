from django.http import HttpResponse
from django.views.generic import ListView
from .models import DatosPokemon
from django.views import View
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

# Presentación Dashboard
# Tabla de los primeros 50 pokémones
class DashboardView(View):
    def get(self, request):
        pokemones = DatosPokemon.objects.all()
        return render(request, "dashboard.html", {"pokemones":pokemones})

# Tabla de los pokémones que pesan entre 30 y 80
class PesoView(View):
    def get(self, request):
        pokemones = DatosPokemon.objects.filter(peso__range=(30, 80))
        return render(request, "peso.html", {"pesoPokemon":pokemones})
# tabla de los pokémones que son tipo grass
class PokemonGrass(View):
    def get(self, request):
        pokemones = DatosPokemon.objects.filter(tipos__icontains="grass")
        return render (request, "tipoGrass.html", {"grassPokemon" : pokemones}) 
#tabla de los pokémones que miden más de 10 y que son tipo flying
class PokemonFlying(View):
    def get(self, request):
        pokemones = DatosPokemon.objects.filter(altura__range = (10, 1000), tipos__icontains = "flying")
        return render(request, "voladores.html", {"voladores" : pokemones})
    
    