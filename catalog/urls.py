from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'catalog'

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>/', views.ProductInfoView.as_view(), name='product_info'),
    path('add_product/', views.AddProductView.as_view(), name='add_product'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
