from django.http import HttpResponse
from catalog.models import Product
from .forms import ProductForm
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.urls import reverse_lazy


class HomeView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        latest_products = Product.objects.order_by('created_at')[:5]
        for product in latest_products:
            print(f"Product: {product.name}, Price: {product.price}")
        return context


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

    def post(self, request):
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse(f'Спасибо, {name}! Сообщение "{message}" получено.')


class ProductInfoView(DetailView):
    model = Product
    template_name = 'catalog/product_info.html'
    context_object_name = 'product'


class AddProductView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/add_product.html'
    success_url = reverse_lazy('catalog:home')
