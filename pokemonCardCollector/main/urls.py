from unicodedata import name
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("cards/", views.cards_index, name="index"),
    path("cards/<int:card_id>/", views.card_detail, name="detail"),
    path("cards/add", views.CardCreate.as_view(), name="card_create"),
    path("cards/<int:pk>/update", views.CardUpdate.as_view(), name="card_update"),
    path("cards/<int:pk>/delete", views.CardDelete.as_view(), name="card_delete"),
    path("cards/<int:card_id>/add_listing", views.add_listing, name="add_listing")
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)