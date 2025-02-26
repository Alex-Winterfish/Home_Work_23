# -*- coding: utf-8 -*-
from django.contrib.auth.models import Group, Permission
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from users.models import CustomUser

class Command(BaseCommand):
    help = "add group admin_products"

    def handle(self, *args, **kwargs):

        user = CustomUser.objects.get(email="product_admin@mail.com")
        group, created = Group.objects.get_or_create(name='admin_products')
        delete_permission = Permission.objects.get(codename='can_delete_product')
        unpublish_permission = Permission.objects.get(codename='can_unpublish_product')
        group.permissions.add(delete_permission, unpublish_permission)
        user.groups.add(group)
        self.stdout.write(self.style.SUCCESS(f'Пользователь {user.username} добавлен в группу admin_products.'))

