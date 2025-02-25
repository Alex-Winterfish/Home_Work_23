# -*- coding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.cache import cache
from django.urls import reverse_lazy
from django.views.generic import (
    DetailView,
    ListView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
)
from .models import Product, Category
from .forms import ProductForm, ModeratorProductForm
from .services import ProductService


class ProductListView(ListView):
    model = Product
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['is_in_group'] = user.groups.filter(name='admin_products').exists()
        return context

    def get_queryset(self):
        queryset = cache.get('my_queryset')
        if not queryset:
            queryset = super().get_queryset()
            cache.set('my_queryset', queryset, 60 * 15)
        return queryset



class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")
    login_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        
        return super().form_valid(form)



class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")
    login_url = reverse_lazy("catalog:product_list")

    def get_form_class(self):
        user = self.request.user
        if user.has_perm("can_unpublish_product"):
            return ModeratorProductForm
        elif self.object.owner == user:
            return ProductForm
        else:
            raise PermissionDenied


class ProductDelete(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")
    login_url = reverse_lazy("catalog:product_list")


class ContactView(TemplateView):
    success_url = reverse_lazy("blog:blog_contacts")
    login_url = reverse_lazy("catalog:product_list")




class CategoryListView(ListView):
    model = Category


class CategoryProductsListView(ListView):
    model = Product
    template_name = "catalog/category_product_list.html"
    context_object_name = "products"

    def get_queryset(self):
        category_id = self.kwargs.get("pk")
        products = ProductService.get_category_product(category_id)
        return products





