# Flask - Python

1. __Pip Install Gunicorn__
   ```
   pip install gunicorn
   ```
2. __Pip Install Postgres Psycopg2__
    ```
    pip install psycopg2
    ```
3. __Create Requirements.txt File__
    ```
    pip freeze > requirements.txt
    ```
4. __Create Procfile__
    ```
    echo web: gunicorn run:app
    ```    
5. __Login To Heroku From The Terminal__
    ```
    heroku login
    ```
6. __Create Heroku App__
    ```
    heroku create <app_name>
    ```
7. __Create Database On Heroku__
    ```
    heroku addons:create heroku-postgresql:hobby-dev --app <app_name>
    ```
8. __Get Database URL And Add To run.py__
    ```
    heroku config --app <app_name>
    ==> copy DATABASE_URL
    set app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    ```
9.  __Save Code To Git__
    ```
    git init
    git add .
    git commit -am "Initial Commit"
    git push
10. __Push Code To Heroku__
    ```
    git push heroku master
    ```
11. __Migrate Database On Heroku__
    ```
    heroku run python manage.py db migrate
    ```

__In a nutshell, do something like this:__

```
from yourapp import create_app
app = create_app()
app.app_context().push()
```

__Some functions inside Flask-SQLAlchemy also accept optionally the application to operate on:__

```
>>> from flaskblog import db, create_app
>>> db.create_all(app=create_app())
```