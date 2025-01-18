from django.urls import path
from catalog.apps import CatalogConfig
from . import views
from .views import ProductListView, ProductDetailView, ProductCreateView, ContactView

app_name = CatalogConfig.name

urlpatterns = [
    path("product_detail/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("product_create/", ProductCreateView.as_view(), name="product_create"),
    path("contacts/", ContactView.as_view(template_name='catalog/contacts.html'), name="contacts"),
    path('products/', ProductListView.as_view(), name='product_list')
]
