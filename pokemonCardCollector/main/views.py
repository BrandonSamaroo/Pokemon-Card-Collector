import imp
from django.shortcuts import render
from django.http import HttpResponse
from .models import PokemonCard

# Create your views here.


def home(request):
    return HttpResponse("INDEX")

def about(request):
    return render(request, 'about.html')

def cards_index(request):
    cards = PokemonCard.objects.all()
    return render(request, 'cards/index.html', {'cards': cards})