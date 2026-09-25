from django.urls import path
from .views import modificar_edad, mi_perfil

urlpatterns = [
    path('modificar_edad/<str:username>/', modificar_edad, name='modificar_edad'),
    path('mi_perfil/<str:username>/', mi_perfil, name="mi_perfil")
]
