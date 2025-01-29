На своём компьютере в директории с проектами создайте папку для проекта YaNews.
Склонируйте проект YaNews из репозитория: git clone …

Для загрузки заготовленных новостей после применения миграций выполните команду:
```bash
python manage.py loaddata news.json
```
Создайте виртуальное окружение 
```bash
python -m venv venv
```
Запустите виртуальное окружение 
```bash
source venv/scripts/activate
```
ОБновить pip
```bash
python.exe -m pip install --upgrade pip
```
и установите зависимости из файла requirements.txt: 
```bash
pip install -r requirements.txt
```
Миграции уже созданы, выполните их: .
```bash
python manage.py migrate
```
Cоздайте суперпользователя: 
```bash
python manage.py createsuperuser
```
Для заполнения базы данных новостями, выполните команду .
```bash
python manage.py loaddata news.json
```
Запустите проект.
```bash
python manage.py runserver
```

```bash

```





