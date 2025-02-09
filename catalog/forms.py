from django import forms
from django.core.exceptions import ValidationError
from .models import Product


class ProductForm(forms.ModelForm):

    restrictions = [
        "казино",
        "криптовалюта",
        "крипта",
        "биржа",
        "дешево",
        "бесплатно",
        "обман",
        "полиция",
        "радар",
        "дёшево",
    ]

    class Meta:
        model = Product
        fields = [
            "product_name",
            "product_description",
            "product_price",
            "category_name"
        ]

    def __init__(self, *args, **kwargs):

        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields["product_name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите название продукта"}
        )

        self.fields["product_description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите описание продукта"}
        )

        self.fields["product_price"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите цену продукта"}
        )

        self.fields["category_name"].widget.attrs.update({"class": "form-control"})

    def clean_product_name(self):
        product_name = self.cleaned_data.get("product_name")

        for restriction in self.restrictions:
            if restriction in product_name.lower():

                raise ValidationError(
                    "Вы используете запрещенные слова в названии продукта"
                )

        return product_name

    def clean_product_description(self):
        product_description = self.cleaned_data.get("product_description")

        for restriction in self.restrictions:

            if restriction in product_description.lower():
                raise ValidationError(
                    "Вы используете запрещенные слова в описании продукта"
                )

        return product_description

    def clean_product_price(self):

        product_price = self.cleaned_data.get("product_price")

        if product_price <= 0:
            raise ValidationError("Цена не может быть меньше или равна нулю")

        return product_price
