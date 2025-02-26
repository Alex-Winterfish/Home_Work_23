from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from .views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ContactView,
    ProductUpdateView,
    ProductDelete,
    CategoryListView, CategoryProductsListView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path(
        "product_detail/<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name="product_detail"
    ),
    path("product_create/", ProductCreateView.as_view(), name="product_create"),
    path(
        "contacts/",
        ContactView.as_view(template_name="catalog/contacts.html"),
        name="contacts",
    ),
    path("products/", ProductListView.as_view(), name="product_list"),
    path(
        "product_update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"
    ),
    path("product_delete/<int:pk>/", ProductDelete.as_view(), name="product_delete"),
    path("categories/", CategoryListView.as_view(), name="category_list"),
    path("category_products/<int:pk>/", CategoryProductsListView.as_view(), name="category_products")
]
