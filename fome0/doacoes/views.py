from django.shortcuts import render, redirect, get_object_or_404
from .models import Restaurante, FoodDonation
from .forms import RestauranteForm, FoodDonationForm

# Página inicial
def home(request):
    return render(request, 'doacoes/home.html')  # Página inicial simples

# View para criar restaurante
def criar_restaurante(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        localizacao = request.POST.get('localizacao')
        
        Restaurante.objects.create(
            nome=nome,
            email=email,
            telefone=telefone,
            localizacao=localizacao
        )
        return redirect('listar_restaurantes')  # Redireciona para a lista de restaurantes
    
    return render(request, 'doacoes/criar_restaurante.html')  # Exibe o formulário

# View para listar restaurantes
def listar_restaurantes(request):
    restaurantes = Restaurante.objects.all()  # Busca todos os restaurantes no banco
    return render(request, 'doacoes/listar_restaurantes.html', {'restaurantes': restaurantes})  # Envia os dados para o template

# View para excluir um restaurante
def excluir_restaurante(request, restaurante_id):
    restaurante = get_object_or_404(Restaurante, id=restaurante_id)
    restaurante.delete()
    return redirect('listar_restaurantes')

# View para adicionar doação de alimento
def add_donation(request, restaurante_id):
    restaurante = get_object_or_404(Restaurante, id=restaurante_id)
    if request.method == 'POST':
        form = FoodDonationForm(request.POST)
        if form.is_valid():
            alimento = form.save(commit=False)
            alimento.restaurante = restaurante
            alimento.save()
            print(f"Alimento salvo: {alimento.nome}, Restaurante: {alimento.restaurante.nome}")  # Depuração
            return redirect('list_donation', restaurante_id=restaurante.id)
    else:
        form = FoodDonationForm()
    return render(request, 'doacoes/add_donation.html', {'form': form, 'restaurante': restaurante})

# View para listar as doações de alimentos de um restaurante
def list_donation(request, restaurante_id):
    restaurante = get_object_or_404(Restaurante, id=restaurante_id)
    alimentos = FoodDonation.objects.filter(restaurante=restaurante)  # Consulta direta no banco
    print(f"Alimentos encontrados: {[alimento.nome for alimento in alimentos]}")  # Depuração
    return render(request, 'doacoes/list_donation.html', {'alimentos': alimentos, 'restaurante': restaurante})

# View para excluir uma doação de alimento
def excluir_alimento(request, alimento_id):
    alimento = get_object_or_404(FoodDonation, id=alimento_id)
    restaurante_id = alimento.restaurante.id
    alimento.delete()
    return redirect('list_donation', restaurante_id=restaurante_id)
