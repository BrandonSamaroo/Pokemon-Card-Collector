from pyexpat import model
from django.db import models

class PokemonCard(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    desc =  models.TextField(max_length=250)
    rarity = models.IntegerField()
    condition = models.IntegerField()
    picture = models.ImageField(upload_to ='images')
