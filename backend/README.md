## AgroRecon

**Running the backend code**

Run the following commands.
```sh
$ cd backend 
```
Install the required packages.
```sh
$ pip install -r requirements.txt
```
Create and apply migrations.
```sh
$ python manage.py makemigrations
$ python manage.py migrate
```
Create superuser.
```sh
$ python manage.py createsuperuser
```
Now run the project using
```sh
$ python manage.py runserver
```
Go to http://127.0.0.1:8000/ in your browser.