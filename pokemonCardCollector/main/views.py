import imp
from django.shortcuts import render
from django.http import HttpResponse
from .models import PokemonCard

# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cards_index(request):
    cards = PokemonCard.objects.all()
    return render(request, 'cards/index.html', {'cards': cards})

def card_detail(request, card_id):
    card =  PokemonCard.objects.get(id=card_id)
    return render(request, "cards/detail.html", {'card': card})