import imp
from turtle import update
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Item, PokemonCard
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ListingForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def cards_index(request):
    cards = PokemonCard.objects.filter(user = request.user)
    return render(request, 'cards/index.html', {'cards': cards})

@login_required
def card_detail(request, card_id):
    card =  PokemonCard.objects.filter(user = request.user).get(id=card_id)
    items_card_doesnt_have = Item.objects.exclude(id__in = card.item.all().values_list('id'))
    listing_form = ListingForm()
    return render(request, "cards/detail.html", {'card': card, 'listing_form': listing_form, 'items': items_card_doesnt_have})

class CardCreate(LoginRequiredMixin, CreateView):
    model = PokemonCard
    fields = ['name', 'type', 'desc', 'rarity', 'condition', 'picture']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CardUpdate(LoginRequiredMixin, UpdateView):
    model = PokemonCard
    fields = '__all__'

class CardDelete(LoginRequiredMixin, DeleteView):
    model = PokemonCard
    success_url = '/cards/'

def add_listing(request, card_id):
    form = ListingForm(request.POST)
    if form.is_valid():
        new_listing = form.save(commit=False)
        new_listing.card_id = card_id
        new_listing.save()
    return redirect('detail', card_id = card_id)

class ItemList(LoginRequiredMixin, ListView):
    model = Item

class ItemDetail(LoginRequiredMixin, DetailView):
    model = Item


class ItemCreate(LoginRequiredMixin, CreateView):
    model = Item
    fields = '__all__'


class ItemUpdate(LoginRequiredMixin, UpdateView):
    model = Item
    fields = '__all__'


class ItemDelete(LoginRequiredMixin, DeleteView):
    model = Item
    success_url = '/items/'

@login_required
def assoc_item(request, card_id, item_id):
    card = PokemonCard.objects.get(id=card_id).item.add(item_id)
    return redirect('detail', card_id=card_id)

@login_required
def unassoc_item(request, card_id, item_id):
    card = PokemonCard.objects.get(id=card_id).item.remove(item_id)
    return redirect('detail', card_id=card_id)


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user =  form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid Signup Try Again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)