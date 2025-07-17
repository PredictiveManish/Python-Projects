# Understanding the folder and the codebase in my language

1. the main directory ```GENAI_QUOTE``` this is the head file
2. after these there subsidary ```genai_quote, quote, manage.py, README.md(this one)``` these files are under the parent file and the genai_quote and quote files are the small applications which combinely works and create a whole application which we will use.
3. ```manage.py``` this file is for managing all the working of application for making migrations, running server etc. 
4. now coming inside the first app `genai_quote` there's `__init__.py` this is initialisation file which makes `genai_quote` becomes a module and easy to import in other places.
- `asgi.py`: Don't know what's this as of now slowly learn and update
- `settings.py`: this manages all the settings in entire application which apps are to be used etc. when we run ```django-admin startproject <project-name>``` then this files automatically generated under `<project-name>` and this files helps to connect multiple dependencies
- `urls.py`: this file helps in connecting and while we run project this gives us right to call different pages based on urls they are assigned like here the localhost port directly opens `home.html` template as it is assigned `\`
- `wsgi.py`: again don't have any knowldge like `asgi.py`

5. coming outside of first application and discussing `quote`: 
- `migrations`: this folder has some important role, but will read and write in my own words
- `templates`: this folder simply contains all the templates which will be used in website and this is the skeleton of the website and covers all the html files.
- `__init__.py`: again initialisation folder helps quote file to be used as a module
- `admin.py`: gives rights to be as an admin (not confident about this)
- `apps.py` : tells about the application configuration 
- `models.py`: no idea again
- `tests.py`: i think for testing puposes
- `urls.py`: manages urls and creating urls for all functions inside the quote application
- `view.py` : this create the view part of the application, it works for rendering etc. and defining the views and how we can view the templates
