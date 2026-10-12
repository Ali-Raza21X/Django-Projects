# Django Task Manager

A simple Todo / Task Management web application built with Django. Users can create tasks, view their task list, update existing tasks, and delete tasks through a clean, centered interface.

## Features

- Create new tasks
- View all tasks
- Update existing tasks
- Delete tasks with a confirmation page
- Django forms and form validation
- SQLite database
- Django template rendering
- Custom CSS styling
- Bootstrap 5 responsive UI
- CSRF protection for form submissions

## Tech Stack

- **Language:** Python
- **Backend:** Django
- **Database:** SQLite
- **Frontend:** HTML, CSS, Bootstrap 5
- **Version Control:** Git and GitHub

## Project Structure

```text
django-todo-app/
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
├── MY_PROJECT/
│   ├── settings.py
│   └── urls.py
└── my_app/
    ├── migrations/
    ├── templates/
    │   ├── base.html
    │   ├── home.html
    │   ├── add_task.html
    │   ├── update.html
    │   └── delete.html
    ├── static/
    │   └── my_app/
    │       └── style.css
    ├── models.py
    ├── views.py
    ├── urls.py
    └── admin.py
```



## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/django-todo-app.git
cd django-todo-app
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

Open the application at:

http://127.0.0.1:8000/

## Usage

1. Open the home page to view tasks.
2. Select **Add New Task** to create a task.
3. Select **Edit** to update an existing task.
4. Select **Delete** to open the confirmation page.
5. Confirm deletion to remove a task.

## Database

This project uses SQLite by default. The local database file is excluded from Git. Django creates the database tables by applying the committed migration files.

## Learning Objectives

This project demonstrates practical experience with:

- Django function-based views
- URL routing
- Django models and ORM
- Forms and ModelForms
- CRUD operations
- Templates and template inheritance
- Static files and CSS
- CSRF protection
- Database migrations
- Git and GitHub workflows

## Future Improvements

- Task completion toggle
- User registration and login
- User-specific tasks
- Task deadlines and priorities
- Search and filtering
- REST API integration
- Deployment to a hosting platform

## Author

**Ali Raza**

GitHub: https://github.com/Ali-Raza21X

