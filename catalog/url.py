# coding=utf-8

from django.conf.urls import url
from .views import product_list, category, product

app_name = 'catalog'

urlpatterns = [
    url(r'^$', product_list, name='product_list'),
    url(r'^(?P<slug>[\w_-]+)$', category, name='category'),
    url(r'^Produto/(?P<slug>[\w_-]+)$', product, name='product'),

]