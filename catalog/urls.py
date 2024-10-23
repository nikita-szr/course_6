from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import (ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView, ProductUnpublishView,
                    ProductCategoryView)

app_name = 'catalog'

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>/', views.ProductInfoView.as_view(), name='product_info'),
    path('', ProductListView.as_view(), name='product_list'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:pk>/unpublish/', ProductUnpublishView.as_view(), name='product_unpublish'),
    path('category/<int:category_id>/', ProductCategoryView.as_view(), name='product_by_category'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
