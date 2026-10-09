from django.urls import path
from .views import mostrar_peliculas

urlpatterns = [
    path('', mostrar_peliculas, name="mostrar_peliculas")
]
