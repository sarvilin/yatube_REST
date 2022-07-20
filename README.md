# Платформа для блогов

Данный проект создан в рамках обучения Яндекс Практикум:

## Описание
Платформа для блогов. Возможность загрузки фото, подписка на авторов,
лента избранных авторов. 
Django REST framework


### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/sarvilin/yatube_REST.git
```
```
cd yatube
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
URL проекта:
```
http://127.0.0.1:8000/
```