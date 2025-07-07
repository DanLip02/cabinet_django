from pathlib import Path
from dotenv import load_dotenv
import os
load_dotenv()

METABASE_URL = os.getenv("METABASE_URL")
METABASE_USER = os.getenv("METABASE_USERNAME")
METABASE_PASS = os.getenv("METABASE_PASSWORD")

DEF_TABLE_URL = os.getenv("DEFAULT_TABLE_URL")
DEF_TABLE_USER = os.getenv("DEFAULT_TABLE_LOGIN")
DEF_TABLE_PASS = os.getenv("DEFAULT_TABLE_PASSWORD")

print(METABASE_URL, METABASE_USER, METABASE_PASS)
# 📁 Базовая директория проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# 🔐 Безопасность
SECRET_KEY = "django-insecure-r&@t&bnhp*7g-k9k)at1r2-@1yy3b85r#@=t!h@1q=%82)d5zm"
DEBUG = True
ALLOWED_HOSTS = []

# 📦 Установленные приложения
INSTALLED_APPS = [
    "dashboard",  # 👈 наше приложение
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

# ⚙️ Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

# 🎨 Шаблоны
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # 👈 добавили путь к шаблонам
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# 💾 База данных (по умолчанию SQLite)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# 🔐 Проверка паролей
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# 🌍 Локализация
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# 📂 Статические файлы (CSS, JS и пр.)
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

# 🧾 Первичный тип ключа
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


#todo there we can start to change smth
# ex. services + log/logout url
# change as you want
# 🔁 Авторизация: редиректы
LOGIN_REDIRECT_URL = "/dashboard/"
LOGOUT_REDIRECT_URL = "/login/"

SERVICES = {
    "Github": {
        "url": "https://github.com",
        "auth": None
    },
    "Metabase": {
        "url": METABASE_URL,
        "auth": (METABASE_USER, METABASE_PASS),
    },
     "Default-table": {
        "url": DEF_TABLE_URL,
        "auth": (DEF_TABLE_USER, DEF_TABLE_PASS),
    },
}