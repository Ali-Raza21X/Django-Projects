# Inventory Management System

A Django-based Inventory Management System.

## Features

- Product management
- Add, view, update, and delete products
- Django templates and custom CSS
- Database operations using Django models

## Requirements

- Python
- Dependencies listed in requirements.txt

## Installation

Open a terminal in the `IMS` directory:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r ..\requirements.txt
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## Project Structure

```text
Inventory Management System/
├── .gitignore
├── README.md
├── requirements.txt
└── IMS/
    ├── manage.py
    ├── IMS/
    └── app/
```

## Status

Under development.
