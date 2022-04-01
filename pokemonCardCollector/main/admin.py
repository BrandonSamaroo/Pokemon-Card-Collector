from django.contrib import admin

from .models import Item, PokemonCard, Listing

# Register your models here.
admin.site.register(PokemonCard)
admin.site.register(Listing)
admin.site.register(Item)