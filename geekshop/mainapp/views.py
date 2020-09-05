import json
import os
import random

from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Product, ProductCategory

JSON_PATH = 'mainapp/json'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)


def get_hot_product():
    products = Product.objects.filter(is_active=True, category__is_active=True)
    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]

    return same_products

def main(request):
    context = {
        'copyright': 'Golubeva Lyubov - GB',
        'title': 'geekshop',
        'products': Product.objects.filter(category__is_active=True)[:4],
        'new_products': Product.objects.all()[3:7],
    }
    return render(request, 'mainapp/index.html', context)

def new(request):
    context = {
        'copyright': 'Golubeva Lyubov - GB',
        'title': 'geekshop',
        'products': Product.objects.all()[3:7],
    }
    return render(request, 'mainapp/index.html', context)

def catalog(request, pk=None, page=1):
    title = 'Catalog'
    links_menu = ProductCategory.objects.filter(is_active=True)

    if pk:
        if pk == '0':
            category = {
                'pk': 0,
                'name': 'all'
            }
            products = Product.objects.filter(is_active=True, category__is_active=True).order_by('price')
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk, is_active=True, category__is_active=True).order_by(
                'price')

        paginator = Paginator(products, 3)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products_paginator,
        }

        return render(request, 'mainapp/products_list.html', content)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    content = {
        'title': title,
        'links_menu': links_menu,
        'hot_product': hot_product,
        'same_products': same_products,
    }

    return render(request, 'mainapp/catalog.html', content)

def contacts(request):
    with open('mainapp/json/contact__locations.json') as f:
        json_data = json.load(f)
    context = {
        'copyright': 'Golubeva Lyubov - GB',
        'title': 'contacts',
        'contact_list': json_data['contacts'],
    }
    return render(request, 'mainapp/contacts.html', context)


def product(request, pk):
    title = 'Product'
    links_menu = ProductCategory.objects.filter(is_active=True)

    product = get_object_or_404(Product, pk=pk)
    same_products = get_same_products(product)


    content = {
        'title': title,
        'links_menu': links_menu,
        'product': product,
        'same_products': same_products,
    }
    return render(request, 'mainapp/product.html', content)
