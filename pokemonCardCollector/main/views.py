import imp
from turtle import update
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import PokemonCard
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ListingForm

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
    listing_form = ListingForm()
    return render(request, "cards/detail.html", {'card': card, 'listing_form': listing_form})

class CardCreate(CreateView):
    model = PokemonCard
    fields = '__all__'

class CardUpdate(UpdateView):
    model = PokemonCard
    fields = '__all__'

class CardDelete(DeleteView):
    model = PokemonCard
    success_url = '/cards/'

def add_listing(request, card_id):
    form = ListingForm(request.POST)
    if form.is_valid():
        new_listing = form.save(commit=False)
        new_listing.card_id = card_id
        new_listing.save()
    return redirect('detail', card_id = card_id)