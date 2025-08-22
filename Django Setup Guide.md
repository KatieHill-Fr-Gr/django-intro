# Django API Setup Guide

## Project Setup

1. Create a folder for your API of choice in your `~/code/ga/labs` folder.

2. Open the folder in VSCode:
   ```bash
   code .
   ```

3. In the terminal, create your virtual environment and install Django simultaneously:
   ```bash
   pipenv install django
   ```

4. Enter the virtual environment shell:
   ```bash
   pipenv shell
   ```

5. Create your project folder:
   ```bash
   django-admin startproject project .
   ```

---

## Setup Environment Variables
We'll use the `django-environ` package in the same way we used `dotenv` in NPM.

1. Install the package:
    ```python
    pipenv install django-environ
    ```

2. Import the package in the `settings.py` file:
    ```python
    # Near the top of the file
    import environ
    ```

3. Add the two lines below the import:
    ```python
    env = environ.Env()
    environ.Env.read_env()
    ```
    These lines give you the `env()` function, which you can use to get the value for any variables inside your `.env` file.

4. Start by securing the SECRET_KEY setting. Add a `SECRET_KEY` variable to your `.env` file, with a strong value:
    ```python
    SECRET_KEY=kjbvcdrtyui9876rfvcdsertyu876tghjiu
    ```

5. Update the `SECRET_KEY` setting in settings.py to the following:
    ```python
    SECRET_KEY = env('SECRET_KEY')
    ```
    This will now use your `.env` variable, and it won't be uploaded to Github.


## Database Setup
1. Create a database on Neon, copy the variables (Parameters Only), and add them to a `.env` file inside your project folder.

2. Update your database configuration in `settings.py`:
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': env('PGDATABASE'),
            'USER': env('PGUSER'),
            'PASSWORD': env('PGPASSWORD'),
            'HOST': env('PGHOST'),
        }
    }
    ```

3. Run your server to test the `DATABASES` setting. If it runs, it’s connected successfully.

---

## Custom Auth Model

1. Create the app:
    ```bash
    django-admin startapp users
    ```

2. Add `users` to `INSTALLED_APPS` in `settings.py`:
    ```python
    INSTALLED_APPS = [
        # All other existing apps
        'users'
    ]
    ```

3. As explained [here in the docs]() we'll subclass AbstractUser, which gives us all the same behaviour as Django's default auth model
    ```python
    from django.contrib.auth.models import AbstractUser

    class User(AbstractUser):
        pass
    ```

4. Add the user to the admin system by defining the following in `admin.py`:
    ```python
    from .models import User

    admin.site.register(User)
    ```

5. Finally, the most important part not to forget, is we'll now tell Django that this is the model we want to use as our Auth model moving forward. Do this BEFORE migrating for the first time:
    ```python
    AUTH_USER_MODEL='users.User'
    ```
    If you altered the name of the model or the app name, then update `users.User` to your `appname.ModelName`.

---

## Install Required Packages

1. Install additional packages:
    ```bash
    pipenv install autopep8 psycopg2-binary djangorestframework
    ```

2. Add `rest_framework` to `INSTALLED_APPS`:
    ```python
    INSTALLED_APPS = [
        # All other existing apps
        'users',
        'rest_framework'
    ]
    ```
    Order isn't important

## Finishing up

1. Run your migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
2. Create an admin user account:
    ```python
    python manage.py createsuperuser
    ```

---

You’re now done with the general setup!
