from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
class Cards:
    def __init__(self, name, type, desc, rarity, condition):
        self.name = name
        self.type = type
        self.desc =  desc
        self.rarity = rarity
        self.condition = condition

cards = [
    Cards("Charizard", "Fire", "Big lizard", .05, 9),
    Cards("Greninja", "Water,Dark", "Sneaky Frog", 1, 8),
]


def home(request):
    return HttpResponse("INDEX")

def about(request):
    return render(request, 'about.html')

def cards_index(request):
    return render(request, 'cards/index.html', {'cards': cards})