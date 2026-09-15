from django.urls import path
from .views import listar_autores


urlpatterns = [
    path('autores/', listar_autores, name='listar_autores'),
]
