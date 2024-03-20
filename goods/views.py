from django.shortcuts import render
from .models import Categories, Products

def catalog(request):
    categories = Categories.objects.all()
    products = Products.objects.all()

    context = {
        "title": "Catalog",
        "categories": categories,
        "products": products
    }
    return render(request, "goods/catalog.html", context=context)