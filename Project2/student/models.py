from django.db import models

# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=70)
    roll=models.IntegerField()
    email=models.EmailField(max_length=255)
    city=models.CharField(max_length=70)

    def __str__(self):
        return self.name

class Result(models.Model):
    stu_class=models.CharField(max_length=70)
    marks=models.IntegerField()

    def __str__(self):
        return self.stu_class

    # python manage.py makemigrations
    # python manage.py migrate
    # python manage.py showmigrations
    # python manage.py sqlmigrate <app_name> <migrations_file_name>