from django.shortcuts import render


def home(request):
    return render(request, 'templates/home/index.html')

def cardapio(request):
    return render(request, 'templates/cardapio/index_cardapio.html')

def servicos(request):
    return render(request, 'templates/servicos/index_servicos.html')

def fotos(request):
    return render(request, 'templates/fotos/index_fotos.html')

def contato(request):
    return render(request, 'templates/contato/index_contato.html')

# definições de views para o cardapio ==============================================
def classic_burger(request):
    return render(request, 'templates/cardapio/classic_burger/index_classic_burger.html')

def special_burger(request):
    return render(request, 'templates/cardapio/special_burger/index_special_burger.html')

def porcoes(request):
    return render(request, 'templates/cardapio/porcoes/index_porcoes.html')

def sobremesas(request):
    return render(request, 'templates/cardapio/sobremesa/index_sobremesa.html')

def bebidas(request):
    return render(request, 'templates/cardapio/bebidas/index_bebidas.html')