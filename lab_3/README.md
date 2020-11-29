# Lab 3
## Хід роботи

1. За допомогою *Django Framework* створив заготовку проекту.
```
pipenv run django-admin startproject test_site
    
        mv test_site/test_site/* test_site/
        mv test_site/manage.py ./

```

2. Запустив сервер та перевірив чи він працює коректно

```
November 29, 2020 - 09:18:06
Django version 3.1.3, using settings 'my_site.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

```
3. Створив шаблон додатку

```
pipenv run python manage.py startapp main
```

4. Створив `main.html` та `urls.py`
5. Заповнив потрібні файли та перевірив правильність їх виконання, модифікував функцію `health`, у результаті при запиті сторінки /health отримуємо відповідь у форматі JSON
6. Створив файл `moitoring.py` який перевіряє доступність серверу раз у хвилину та записує інформацію у відповідний файл
7. Спростив роботу за допомогою Pipenv файлом:
```
server = "python manage.py runserver"
monitoring = "python3 monitoring.py"
```