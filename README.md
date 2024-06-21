# Проект «QRKot»
![python version](https://img.shields.io/badge/Python-3.9-green)

## О проекте

QRKot - это благотворительный фонд поддержки котиков. Наша цель - сбор пожертвований для различных целевых проектов, таких как медицинское обслуживание, обустройство кошачьих колоний и обеспечение кормом. Мы стремимся помочь нуждающимся кошкам получить всё необходимое для комфортной жизни.

## Ключевые функции

- Управление проектами: Возможность создавать, редактировать и удалять целевые проекты;
- Система пожертвований: Пожертвования распределяются по принципу First In, First Out, обеспечивая приоритетность ранним проектам;
- Прозрачность и доступность: Все пользователи могут просматривать списки проектов и пожертвований;
- Авторизация и аутентификация: Защита данных пользователей и проектов с использованием JWT.

## Установка и запуск

Клонировать репозиторий и перейти в него в командной строке:

```
https://github.com/krupindi/cat_charity_fund.git
```

```
cd cat_charity_fund
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Создать и заполнить .env файл по шаблону .env_template

```
APP_TITLE=...
APP_DESCRIPTION=...
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
SECRET=...
FIRST_SUPERUSER_EMAIL=...
FIRST_SUPERUSER_PASSWORD=...
```

Выполнить миграции:

```
alembic upgrade head
```

Запустить приложение:

```
uvicorn app.main:app --reload
```

- Swagger - http://127.0.0.1:8000/docs
- Redoc - http://127.0.0.1:8000/redoc

Использовать Postman для тестирования и отладки работы API (собенности запуска и настройки коллекции описаны в файле /postman_collection/README.md )

## Автор проекта

Крупин Дмитрий