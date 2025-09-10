# Vesttern — сайт-конструктор одежды

Vesttern — это веб-сайт, разработанный на **Django**, который демонстрирует услуги по разработке лекал и конструкторской работе в сфере моды.  
Целевая аудитория: бренды одежды, производства и начинающие дизайнеры.

## 🚀 Функционал

- Главная страница с описанием услуг и преимуществ  
- Разделы: **Разработка, Сопровождение, Размножение, Портфолио**  
- Модульные шаблоны (навигация и футер подключаются на все страницы)  
- Адаптивный дизайн с использованием **Bootstrap 5**  
- Статические файлы и кастомные стили (`style.css`)  
- Логотип и брендирование  

## 🛠 Технологии

- **Python 3.10+**  
- **Django 4+**  
- **Bootstrap 5**  
- **HTML5 / CSS3**  

## 📂 Структура проекта
vesttern/
├── manage.py
├── vesttern/ # настройки проекта
├── core/ # основное приложение
│ ├── templates/core/
│ │ ├── base.html
│ │ ├── nav.html
│ │ ├── footer.html
│ │ ├── index.html
│ │ ├── development.html
│ │ ├── support.html
│ │ ├── replication.html
│ │ └── portfolio.html
│ └── static/core/
│ ├── css/style.css
│ └── img/logo.jpg


## ⚙️ Установка и запуск
## 📦 Установка и запуск

# 1. Клонируйте репозиторий
git clone https://github.com/ka-uko/dj02project_vesttern.git
cd vesttern

# 2. Создайте виртуальное окружение и активируйте его
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

# 3. Установите зависимости
pip install -r requirements.txt

# 4. Примените миграции
python manage.py migrate

# 5. Запустите сервер разработки
python manage.py runserver

