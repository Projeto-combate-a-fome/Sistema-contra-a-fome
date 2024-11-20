from django import forms
from .models import Restaurante, FoodDonation

# Formulário para Restaurante
class RestauranteForm(forms.ModelForm):
    class Meta:
        model = Restaurante
        fields = ['nome', 'email', 'telefone', 'localizacao']

# Formulário para Alimento
class FoodDonationForm(forms.ModelForm):
    class Meta:
        model = FoodDonation
        fields = ['nome', 'quantidade', 'descricao']

    # Caso deseje tornar a descrição obrigatória
    descricao = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))

