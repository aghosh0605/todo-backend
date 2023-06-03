# todo-backend

## Important Commands to setup project

```bash
python3 -m venv env               # Set up a virtual environment
source env/bin/activate           #	Activate the virtual environment
python -m pip install django
python -m pip freeze > requirements.txt        # Install Django
python -m pip install -r requirements.txt      # Pin your dependencies
django-admin startproject backend       # Set up a Django project
python manage.py startapp todo          # Start a Django app
python3 manage.py makemigrations  # Responsible for creating new migrations based on the changes you have made to your models
python3 manage.py migrate   # Responsible for applying and unapplying migrations.
python3 manage.py runserver         # TO start the server
```

**Django Admin Dashboard Username and Password**

- username: admin
- password: github
