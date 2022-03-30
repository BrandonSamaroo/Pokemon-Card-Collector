from django.db import models
from django.urls import reverse

class PokemonCard(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    desc =  models.TextField(max_length=250)
    rarity = models.IntegerField()
    condition = models.IntegerField()
    picture = models.ImageField(upload_to ='images')
    def get_absolute_url(self):
        return reverse("detail", kwargs={"card_id": self.id})
    def __str__(self):
        return f"{self.name}"
    class Meta:
        ordering = ['rarity']

class Listing(models.Model):
    name = models.CharField(max_length=100)
    site = models.URLField()
    card = models.ForeignKey(PokemonCard, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.card} listing on {self.name} link: {self.site}" #get display is a built in function for displaying choices
    class Meta:
        ordering = ['name']