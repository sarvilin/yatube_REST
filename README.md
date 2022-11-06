# API для платформы блогов

## Описание
Позволяет делать запросы к базе данных. Поддерживаются все функции
основного проекта: регистрация пользователей, получение списка постов,
отдельного поста, создание постов и комментариев, подписки.
Авторизация по JWT-токенам при помощи Djoser.

## Технологии
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)

### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/sarvilin/yatube_REST.git
```
```
cd yatube_REST
```

Cоздать и активировать виртуальное окружение:
```
python3 -m venv venv
```
```
source venv/bin/activate
```
```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
Сгенерировать и указать SECRET_KEY:
```
создать файл:  yatube_REST/yatube_api/yatube_api/.env
добавить строку: SECRET_KEY = '<ВАШ СЕКРЕТНЫЙ КЛЮЧ>'
```
Выполнить миграции:
```
python3 yatube_api/manage.py migrate
```
Запустить проект:
```
python3 yatube_api/manage.py runserver
```

URL проекта:  http://127.0.0.1:8000/

### *Backend by:*
[Сарвилин Алексей](https://github.com/sarvilin/yatube_REST)

Данный проект создан в рамках обучения Яндекс Практикум