"""delivery_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import home, cardapio, servicos, fotos, contato

# import para Cardapio
from .views import  classic_burger, special_burger, porcoes, sobremesas, bebidas


urlpatterns = [
    path('', home, name='home'),
    path('Catalogo/', include('catalog.url', namespace='catalog')),
    path('Cardapio/', cardapio, name='cardapio'),
    path('Servicos/', servicos, name='servicos'),
    path('Fotos/', fotos, name='fotos'),
    path('Contato/', contato, name='contato'),

    # Urls para o cardapio ========================================

    path('classic-burger/', classic_burger, name='classic-burger'),
    path('special-burger/', special_burger, name='special-burger'),
    path('porcoes/', porcoes, name='porcoes'),
    path('sobremesas/', sobremesas, name='sobremesas'),
    path('bebidas/', bebidas, name='bebidas'),

    # End / Urls para cardapio ====================================

    path('admin/', admin.site.urls),
]