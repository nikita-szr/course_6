from django.shortcuts import render, redirect
from django.http import HttpResponse
from catalog.models import Product
from .forms import ProductForm


def home(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    latest_products = Product.objects.order_by('created_at')[:5]
    for product in latest_products:
        print(f"Product: {product.name}, Price: {product.price}")
    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse(f'Спасибо, {name}! Сообщение "{message}" получено.')
    return render(request, 'catalog/contacts.html')


def product_info(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        'product': product
    }
    return render(request, 'catalog/product_info.html', context)


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalog:home')
    else:
        form = ProductForm()
    return render(request, 'catalog/add_product.html', {'form': form})
