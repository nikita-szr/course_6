from django.http import HttpResponse, HttpResponseForbidden
from catalog.models import Product
from .forms import ProductForm
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from .services import ProductService
from .models import Category


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


@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductInfoView(DetailView):
    model = Product
    template_name = 'catalog/product_info.html'
    context_object_name = 'product'


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('catalog:home')
    login_url = 'users:login'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('catalog:home')
    login_url = 'users:login'

    def update_func(self):
        product = self.get_object()
        return self.request.user == product.owner or self.request.user.groups.filter(name='Moderators').exists()


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('catalog:home')
    login_url = 'users:login'

    def delete_func(self):
        product = self.get_object()
        return self.request.user == product.owner or self.request.user.groups.filter(name='Moderators').exists()



    def delete(self, request, *args, **kwargs):
        if not request.user.has_perm('catalog.delete_product'):
            return HttpResponseForbidden("У вас нет прав для удаления этого продукта.")

        return super().delete(request, *args, **kwargs)


class ProductUnpublishView(PermissionRequiredMixin, View):
    permission_required = 'catalog.can_unpublish_product'
    template_name = 'catalog/product_unpublish_confirm.html'

    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        return self.render_to_response({'product': product})

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        if not request.user.has_perm('catalog.can_unpublish_product'):
            return HttpResponseForbidden("У вас нет прав для отмены публикации этого продукта.")

        product.is_published = False
        product.save()
        return redirect('product_list')


class ProductCategoryView(ListView):
    model = Product
    template_name = 'catalog/product_category_list.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        category_id = self.kwargs['category_id']

        context['products'] = ProductService.get_products_by_category(category_id)
        context['category_name'] = ProductService.get_category_name(category_id)
        return context
