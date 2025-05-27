from django.db import models

class Profile(models.Model):
    name=models.CharField(max_length=70)
    roll=models.IntegerField()
    email=models.EmailField(max_length=255)
    city=models.CharField(max_length=70)

class Result(models.Model):
    stu_class=models.CharField(max_length=70)
    marks=models.IntegerField()

class User(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    password=models.CharField(max_length=255)