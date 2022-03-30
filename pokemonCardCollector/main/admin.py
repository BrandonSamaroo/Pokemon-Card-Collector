from django.contrib import admin

from .models import PokemonCard, Listing

# Register your models here.
admin.site.register(PokemonCard)
admin.site.register(Listing)