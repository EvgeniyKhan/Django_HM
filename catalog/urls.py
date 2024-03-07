from django.urls import path

from catalog.views import index, contacts, products_detail

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/', products_detail, name='products_detail'),
]
