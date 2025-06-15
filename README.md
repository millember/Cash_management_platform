1. Клонировать репозиторий:
git clone https://github.com/millember/Cash_management_platform.git
2. Создать и активировать виртуальное окружение:
python -m venv venv
Linux/Mac:
source venv/bin/activate
Windows:
venv\Scripts\activate
3. Установить зависимости:
pip install -r requirements.txt
4. Создайте базу данных и пользователя:
sudo -u postgres psql
CREATE DATABASE management;
CREATE USER niyazdb WITH PASSWORD 'qwerty';
5.Настройте подключение в Django:
Откройте config/settings.py и убедитесь в наличии:
DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "management",
        "USER": "niyazdb",
        "PASSWORD": "qwerty",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
6. Настроить базу данных:
python manage.py makemigrations management
python manage.py migrate
7. Создать суперпользователя (опционально):
python manage.py createsuperuser
8. Загрузка базы данных с помощью loaddata:
python manage.py loaddata model_backup.json
9. Запустить сервер:
python manage.py runserver
10. Открыть в браузере:
http://localhost:8000/
11.Для доступа к админ-панели:
http://localhost:8000/admin/
