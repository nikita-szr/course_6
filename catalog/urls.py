from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('home/', views.home, name='home'),  # Главная
    path('contacts/', views.contacts, name='contacts')  # Контакты
]
