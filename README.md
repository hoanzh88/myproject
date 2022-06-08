# myproject
Django CRUD with forms, teamplate

### Install Mysql python (nếu chưa có)
pip3 install pymysql

### Start project
python -m django startproject myproject

\myproject\settings.py
```
import pymysql
pymysql.install_as_MySQLdb()

### Cấu hình database MySql
settings.py
```
DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.mysql',
       'NAME': 'django',
       'USER': 'root',
       'PASSWORD': '',
       'HOST': 'localhost',
       'PORT': '',
   }
}
```
```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Tạo module (app) mới
python manage.py startapp posts

### đăng ký cho module mới tạo vào trong hệ thống
```
settings.py
```
INSTALLED_APPS = [
   'posts',
```

posts/models.py
```
from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse

class Post(models.Model):
  name = models.CharField(max_length=224, null=False, blank=False)
  content = models.TextField(max_length=254, null=False, blank=False)
  timestamp = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  def __unicode__(self):
    return self.content
```

```
python manage.py makemigrations
python manage.py migrate
```