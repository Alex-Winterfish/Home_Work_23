from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=150, verbose_name="Категория")
    category_description = models.TextField()

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категория'
        ordering = ['category_name']


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name="Наименование")
    product_description = models.TextField(max_length=200, verbose_name="Описание")
    product_image = models.ImageField()
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    product_price = models.IntegerField()
    created_at = models.DateField()
    updated_at = models.DateField()

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['product_name', 'category_name']




