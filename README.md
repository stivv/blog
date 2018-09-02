This is a blog template done to give you a head on developing a blog using python django.

How to install

1. Install django. Go to https://www.djangoproject.com/ for more details.
2. After installing django on your computer and creating a project, clone this repo inside your project.
3. Go to setting.py inside your project folder and under "INSTALLED_APPS", add 'blog.apps.BlogConfig'
4. Then go to urls.py inside your project folder and add ""path('blog/', include('blog.urls')),"" to urlpatterns.
5. On your terminal/cmd run python manage.py migrate
6. Then run python manage.py createsuperuser (if you haven't yet).
7. Then run python manage.py runserver
8. Go to http://127.0.0.1:8000/blog to access the blog and http://127.0.0.1:8000/admin (user the credentials you entered on step 6) to manage the log site.

Thats it!