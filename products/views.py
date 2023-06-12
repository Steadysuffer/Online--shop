from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return render(request, 'products/index.html', {'title': 'BIG SMOKE'})


def products(request):
    return render(request, 'products/products.html', {'title': 'PRODUCTS'})
