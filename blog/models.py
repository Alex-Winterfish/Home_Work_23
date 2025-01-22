# -*- coding: utf-8 -*-
from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок статьи")
    content = models.TextField(max_length=1000, verbose_name="Текст статьи")
    preview = models.ImageField(upload_to='blog/', verbose_name="Изображение", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publish_attribute = models.BooleanField(default=True, verbose_name="Признак публикации")
    view_count = models.PositiveIntegerField(default=0, verbose_name="Количество просмотров")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "статья"
        verbose_name_plural = "статьи"
        ordering = ["title"]