# 🏦 Cash Management Platform (CMP)

**Система учета движения денежных средств** - полнофункциональное веб-приложение для управления финансовыми операциями с поддержкой справочников, аналитики и сложных бизнес-правил.


## 🔍 Основные возможности

- 💰 Учет приходных/расходных операций
- 🏷️ Гибкая система категорий и подкатегорий
- 🔗 Соблюдение бизнес-правил:
  - Контроль связи подкатегорий с категориями
  - Контроль связи категорий с типами операций
- 📊 Фильтрация и аналитика
- 🛡️ Валидация данных на клиенте и сервере

## 🛠 Технологический стек

**Backend:**
- Python 3.10+
- Django 4.2+
- PostgreSQL 14+
- Django REST Framework (API)

**Frontend:**
- Bootstrap
- jQuery (AJAX)
- Chart.js (аналитика)

## 🚀 Быстрый старт

### 1. Установка зависимостей

```bash
# Создание виртуального окружения (Linux/macOS)
python3 -m venv venv
source venv/bin/activate

# Установка зависимостей
pip install -r requirements.txt
```
### 2. Настройка базы данных

```bash
# Создайте БД в PostgreSQL
sudo -u postgres psql -c "CREATE DATABASE cmp_db;"
sudo -u postgres psql -c "CREATE USER cmp_user WITH PASSWORD 'securepass123';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE cmp_db TO cmp_user;"

# Настройте подключение в .env переименовав .env.sample :
NAME=       #Название базы данных
USER_DB=    #Имя пользователя базы данных
PASSWORD=   #Пароль от базы данных
HOST=       #Хост
PORT=       #Порт
```
### 3. Запуск приложения
```bash
# Применение миграций
python manage.py migrate

# Создание суперпользователя
python manage.py createsuperuser

# Запуск сервера разработки
python manage.py runserver
Приложение будет доступно по адресу: http://localhost:8000
```
## 📂 Структура проекта
```text
cash-management-platform/
├── config/               # Настройки Django
│   ├── settings.py       # Конфигурация приложения
│   └── urls.py           # Главные URL-маршруты
├── management/           # Основное приложение
│   ├── forms.py          # Формы
│   ├── services.py       # Сервисный слой
│   ├── models.py         # Модели данных
│   └── views.py          # Контроллеры
├── static/               # Статические файлы
├── templates/            # Базовые шаблоны
├── requirements.txt      # Зависимости
├── .env                  # Данные для подключения к базе данных
└── manage.py
```