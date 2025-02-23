# Домашняя работа 24

Зависимости:
```
pip install -r /path/to/requirements.txt
```
Для обновления базы данных выполнить команду:

python manage.py add_product

Запуск сервера:

python manage.py runserver

Добавлена возможность добавления продукта. Для этого на вкладе "добавление продукта" заполнить форму

добавлен подшаблон menu.html.

# Домашняя работа 25
Контроллеры в приложении Catalog переведены в CBV

Написано проложение Blog

заполнить базу данных из фикстуры blog_fixture.json
```commandline
python manage.py loaddata blog_fixture.json --format json 
```
# Доработка
- в моделях Product и BlogPost добавлены параметры в ImageField 
- исправлены адреса в подшаблоне menu проложения blog
- при вызове DetailView в приложениях blog и catalog изображения корректно отображаются
Для заполнения базы данных через фикстуры:
```commandline
python manage.py loaddata category_fixture.json --format json
python manage.py loaddata product_fixture.json --format json
python manage.py loaddata blog_fixture.json --format json
```

# Домашняя работа 26.1

- реализован CRUD с использованием django.form
- реализованна валидация полей Название продукта, Описание продукта и Цена продукта

# Домашняя работа 27
Для заполнения базы данных через фикстуры:
```commandline
python manage.py loaddata category_fixture.json --format json
python manage.py loaddata product_fixture.json --format json
```

Реализованна регистрация и аутентификация пользователей в приложении Catalog. При регистрации нового пользователя на почту высылается приветственное письмо.

В файле .env.sample указаны необходимые переменные окружения 

# Домашняя работа 28

Для проверки:
1. Заполнить базу данных через фикстуры:
```
python manage.py loaddata category_fixture.json --format json
python manage.py loaddata product_fixture.json --format json
python manage.py loaddata users_fixture.json --format json
```
Создаются пользователи:

- Alksbulgakov@gmail.com пароль 12345 - имеет права суперпользователя
- milk_merchant@mail.com пароль qwer12345678 - продавец молочных продуктов
- meat_merchant@mail.com пароль qwer12345678 - продавец мясных продуктов
- candy_merchant@mail.com пароль qwer12345678 - продавец кондитерских изделий
- product_admin@mail.com пароль qwer12345678 - модератор продуктов

2. Выполнить кастомную команду 
```commandline
python manage.py add_group
```
создается группа admin_products с правами на удаление и публикацию продукта, пользователь product_admin@mail.com добавляется в группу admin_products