from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'catalog'

urlpatterns = [
    path('home/', views.home, name='home'),  # Главная
    path('contacts/', views.contacts, name='contacts'),  # Контакты
    path('product/<int:product_id>/', views.product_info, name='product_info'),  # Информация о товаре
    path('add_product/', views.add_product, name='add_product')  # Добавление товара
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
