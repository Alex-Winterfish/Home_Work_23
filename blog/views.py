from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, TemplateView
from .models import BlogPost
class PostListView(ListView):
    model = BlogPost
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(publish_attribute=True)


class PostDetailView(DetailView):
    model = BlogPost
    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object

class PostCreateView(CreateView):
    model = BlogPost
    fields = ['title', 'content', 'publish_attribute']
    success_url = reverse_lazy('blog:posts')