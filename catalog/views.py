from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, TemplateView
from .models import Product

class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product

class ProductCreateView(CreateView):
    model = Product
    fields = ['product_name', 'product_description', 'product_price', 'category_name']
    success_url = reverse_lazy('catalog:product_list')


class ContactView(TemplateView):
    success_url = reverse_lazy('blog:blog_contacts')

