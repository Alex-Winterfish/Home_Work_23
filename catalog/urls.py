from django.urls import path
from catalog.apps import CatalogConfig
from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path('product_info/', views.product_info, name='product_info'),
    path('product_list/', views.product_list, name='product_list')
]