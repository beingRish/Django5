from django.db import models
from django.urls import reverse

class Student(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField()
    course = models.CharField(max_length=70)

class Candidate(models.Model):
    name = models.CharField()
    email = models.EmailField()
    password = models.CharField() 

    def get_absolute_url(self):
        return reverse("thanks")
    