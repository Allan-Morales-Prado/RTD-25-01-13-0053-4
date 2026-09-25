from django.urls import path
from .views import listar_posts

urlpatterns = [
    path('', listar_posts, name='blog_listar_post')
]
