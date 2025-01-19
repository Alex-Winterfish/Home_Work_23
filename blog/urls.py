from django.urls import path
from blog.apps import BlogConfig
from .views import PostListView, PostDetailView, PostCreateView

app_name = BlogConfig.name

urlpatterns = [
    path("posts_list/", PostListView.as_view(), name='posts'),
    path("post_detail/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("post_create/", PostCreateView.as_view(), name="post_create")
]