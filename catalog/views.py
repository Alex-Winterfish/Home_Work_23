from django.urls import reverse_lazy
from django.views.generic import (
    DetailView,
    ListView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
)
from .models import Product
from .forms import ProductForm


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")


class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")


class ContactView(TemplateView):
    success_url = reverse_lazy("blog:blog_contacts")
