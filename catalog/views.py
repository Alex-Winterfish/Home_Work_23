# -*- coding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    DetailView,
    ListView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
)
from .models import Product
from .forms import ProductForm, ModeratorProductForm


class ProductListView(ListView):
    model = Product


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
        else:
            return ProductForm


class ProductDelete(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")
    login_url = reverse_lazy("catalog:product_list")


class ContactView(TemplateView):
    success_url = reverse_lazy("blog:blog_contacts")
    login_url = reverse_lazy("catalog:product_list")


class PublishProductView(LoginRequiredMixin, View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)

        if not request.user.has_perm("can_unpublish_product"):
            return HttpResponseForbidden("У вас нет прав доступа для публикации продукта")

        product.publish_attribute = True
        product.save()

        return redirect("products:product_list")
