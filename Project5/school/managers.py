from django.db import models



# class CustomStudentManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().order_by('name')



class CustomStudentManager(models.Manager):
    def get_stu_roll_range(self, r1, r2):
        return super().get_queryset().filter(roll__range=(r1, r2))
    