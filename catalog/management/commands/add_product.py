# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Add product to the database"

    def handle(self, *args, **kwargs):
        Category.objects.all().delete()
        Product.objects.all().delete()
        category, _ = Category.objects.get_or_create(
            category_name="Кондитерские изделия",
            category_description="Продукты с большим содержанием сахара",
        )

        products = [
            {
                "product_name": "Ириска",
                "product_description": "Помадная масса, получаемая при уваривании сгущённого молока с сахаром, "
                "мелассой (патокой) и жиром (сливочным или растительным маслом либо маргарином)."
                "Вязкая конфета из патоки и битума, для удаления зубных пломб. "
                "Употреблять с осторожностью",
                "product_image": "butterscotch.jpg",
                "product_price": 54,
                "category_name": category,
            },
            {
                "product_name": "Вафли",
                "product_description": "разновидность тонкого сухого печенья с оттиском на поверхности. "
                "Выпекается из взбитого жидкого теста в специальных формах. "
                "Тесто состоит из муки, яиц, сахара (в сладких вафлях) и сливок.",
                "product_price": 43,
                "product_image": "vaffels.jpg",
                "category_name": category,
            },
            {
                "product_name": "Леденцы",
                "product_description": "Долгоиграющая конфета из патоки. Вид твёрдых конфет, "
                "обычно состоящих из ароматизированного сахара с патокой или кукурузным сиропом",
                "product_image": "lolypop.jpg",
                "product_price": 54,
                "category_name": category,
            },
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully added student: {product.product_name}"
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f"Product already exists: {product.product_name}"
                    )
                )

        category, _ = Category.objects.get_or_create(
            category_name="Молочные продукты",
            category_description="Продуты из молока домашних животных",
        )

        products = [
            {
                "product_name": "Творог",
                "product_description": "нежидкий кисломолочный продукт белого цвета, традиционный для Восточной, "
                "Северной и (реже) Центральной Европы, получаемый сквашиванием молока с"
                " последующим удалением сыворотки. Официально принято классифицировать творог, "
                "выработанный традиционным способом, по содержанию в нём жира.",
                "product_image": "cottage_cheese.jpg",
                "product_price": 54,
                "category_name": category,
            },
            {
                "product_name": "Сметна 15%",
                "product_description": " пастообразный кисломолочный продукт. Производят из сливок, сквашенных "
                "молочнокислыми бактериями. Название пошло от слов «снимать» или «сметать» — "
                "имеется в виду верхушка со скисшего молока, из которого потом получали сметану."
                "Кисломолочный продукт 15% жирности",
                "product_price": 43,
                "product_image": "sour_cream.jpg",
                "category_name": category,
            },
            {
                "product_name": "Молоко",
                "product_description": "ценный пищевой продукт, содержащий более 100 питательных веществ,"
                " включая белки, жир, молочный сахар, минеральные вещества, фосфолипиды, "
                "органические кислоты, витамины, ферменты.",
                "product_price": 54,
                "product_image": "milk.jpg",
                "category_name": category,
            },
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully added student: {product.product_name}"
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f"Product already exists: {product.product_name}"
                    )
                )

        category, _ = Category.objects.get_or_create(
            category_name="Мясные продукты",
            category_description="Продукты из мяса домашних животных",
        )

        products = [
            {
                "product_name": "Докторская колбаса",
                "product_description": "Докторская колбаса, производится по ГОСТу с использованием отборной свинины "
                "и говядины высшего сорта. Продукт приготовлен в оболочке полиамид, "
                "что придает ему чуть более упругую консистенцию, а во вкусе возможность "
                "ощутить натуральный вкус мяса, подчеркнутый ароматом кардамона, без копчения."
                "Вареная колбаса из отходов "
                "мясного производства",
                "product_price": 54,
                "category_name": category,
            },
            {
                "product_name": "Московская",
                "product_description": "Колбаса Московская сделана по ГОСТу из отборной говядины, "
                "хребтового шпика крупного помола и всего лишь двух специй: "
                "черного перца и кардамона. Благодаря этому вы можете насладиться "
                "натуральным насыщенным вкусом говядины и превосходным ароматом "
                "настоящей колбасы. Сырокопченая колбаса из отходов мясного"
                " производства",
                "product_price": 43,
                "category_name": category,
            },
            {
                "product_name": "Нарезка индилайт",
                "product_description": "Мясной продукт из бедер индейки. Индейка — диетический продукт. "
                "Так что нарезка особенно понравится тем, кто считает калории. "
                "Помимо мяса, в составе только соль. Нежное филе индейки, нарезанное "
                "аккуратными слайсами, отлично подойдёт как для мясной тарелки, "
                "так и для сытного перекуса.",
                "product_price": 54,
                "category_name": category,
            },
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully added student: {product.product_name}"
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f"Product already exists: {product.product_name}"
                    )
                )
