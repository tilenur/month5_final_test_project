# Blog API

REST API project built with Django REST Framework.

## Features

- Posts CRUD
- Comments CRUD
- Token Authentication
- Permissions system
- Nested comments endpoints
- Swagger documentation
- PostgreSQL database

## Technologies

- Python
- Django
- Django REST Framework
- PostgreSQL
- drf-yasg

## Installation

Clone repository:

```bash
git clone <repository_link>
```

Create virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Apply migrations:

```bash
python manage.py migrate
```

Run server:

```bash
python manage.py runserver
```

## API Documentation

Swagger:
```text
http://127.0.0.1:8000/swagger/
```

ReDoc:
```text
http://127.0.0.1:8000/redoc/
```
