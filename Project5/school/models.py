from django.db import models
from school.managers import CustomStudentManager

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField(unique=True, null=False)
    city = models.CharField(max_length=70)
    marks = models.IntegerField()
    pass_date = models.DateField()
    admission_date = models.DateTimeField()

    objects = CustomStudentManager()


# # Custom Manager in Proxy Model
# class ProxyStudent(Student):
#     objects = CustomStudentManager()
#     class Meta:
#         proxy = True
#         ordering = ['name']