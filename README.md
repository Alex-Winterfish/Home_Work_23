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
- Для заполнения базы данных через фикстуры:
```commandline
python manage.py loaddata category_fixture.json --format json
python manage.py loaddata product_fixture.json --format json
python manage.py loaddata blog_fixture.json --format json
```

