from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Product, Category


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
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        return HttpResponse(f'Спасибо, {name}! Сообщение получено.')
    return render(request, 'catalog/contacts.html')


def product_info(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        'product': product
    }
    return render(request, 'catalog/product_info.html', context)
