from django.urls import path
from catalog.apps import CatalogConfig
from . import views
from .views import ProductListView

app_name = CatalogConfig.name

urlpatterns = [
    path("product_info/<int:product_id>/", views.product_info, name="product_info"),
    path("add_product/", views.add_product, name="add_product"),
    path("contacts/", views.contacts, name="contacts"),
    path('product/', ProductListView.as_view(), name='product_list')
]
