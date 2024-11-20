from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página inicial
    path('criar_restaurante/', views.criar_restaurante, name='criar_restaurante'),
    path('listar/', views.listar_restaurantes, name='listar_restaurantes'),
    path('excluir_restaurante/<int:restaurante_id>/', views.excluir_restaurante, name='excluir_restaurante'),
    path('add_donation/<int:restaurante_id>/', views.add_donation, name='add_donation'),
    path('list_donation/<int:restaurante_id>/', views.list_donation, name='list_donation'),
    path('excluir_alimento/<int:alimento_id>/', views.excluir_alimento, name='excluir_alimento'),
]
