from django.shortcuts import render, HttpResponse

from products.models import ProductCategory, Product


def index(request):
    context = {
        'title': 'DrinkNoThink - магазин зельеварения',
        'is_promotion': True,
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Ассортимент',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)
