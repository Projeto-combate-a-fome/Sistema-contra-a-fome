from django.db import models
from django.utils import timezone
from datetime import timedelta

# Modelo para Restaurante
class Restaurante(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    email = models.EmailField(verbose_name="E-mail")
    telefone = models.CharField(max_length=15, verbose_name="Telefone")
    localizacao = models.CharField(max_length=255, verbose_name="Localização")
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")

    def __str__(self):
        return self.nome

# Modelo para Doação de Alimento
class FoodDonation(models.Model):
    restaurante = models.ForeignKey(
        Restaurante,
        on_delete=models.CASCADE,
        related_name='doacoes',
        verbose_name="Restaurante"
    )
    nome = models.CharField(max_length=100, verbose_name="Nome do Alimento")
    quantidade = models.PositiveIntegerField(verbose_name="Quantidade")
    descricao = models.TextField(blank=True, verbose_name="Descrição do Alimento")
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Cadastro")

    def is_valid(self):
        """
        Verifica se a doação ainda é válida.
        Neste caso, consideramos a validade de 7 dias.
        """
        validade = self.data_criacao + timedelta(days=7)
        return timezone.now() <= validade

    def __str__(self):
        return f"{self.nome} - {self.quantidade} unidades"

