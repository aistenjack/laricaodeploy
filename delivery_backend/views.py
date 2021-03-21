from django.shortcuts import render


def home(request):
    return render(request, 'index.html')

def cardapio(request):
    return render(request, 'index_cardapio.html')

def servicos(request):
    return render(request, 'index_servicos.html')

def fotos(request):
    return render(request, 'index_fotos.html')

def contato(request):
    return render(request, 'index_contato.html')

# definições de views cardapio ==============================================
def classic_burger(request):
    return render(request, 'cardapio/index_classic_burger.html')

def special_burger(request):
    return render(request, 'cardapio/index_special_burger.html')

def porcoes(request):
    return render(request, 'cardapio/index_porcoes.html')

def sobremesas(request):
    return render(request, 'cardapio/index_sobremesa.html')

def bebidas(request):
    return render(request, 'cardapio/index_bebidas.html')