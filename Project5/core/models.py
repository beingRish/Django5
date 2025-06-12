from django.db import models



# Abstract Model Inheritance
class BaseModel(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    join_date = models.DateField()

    class Meta:
        abstract = True

class Student(BaseModel):
    fees = models.IntegerField()
    join_date = None

class Teacher(BaseModel):
    salary = models.IntegerField()

class Contractor(BaseModel):
    payment = models.IntegerField()
    join_date = models.DateTimeField()



# Multi Table Inheritance
class ExamCenter(models.Model):
    center_name = models.CharField(max_length=255)
    center_city = models.CharField(max_length=255)

class Candidate(ExamCenter):
    name = models.CharField(max_length=255)
    roll = models.IntegerField()



# Proxy Model
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    stock = models.IntegerField()

class DiscountedProduct(Product):
    class Meta:
        proxy = True
        ordering = ['id']
