from django.db import models

# Create your models here.

class teacher (models.Model):
    Name = models.CharField(max_length=25)
    Area = models.CharField(max_length=30)

class course_Area (models.Model):
    Achivement_standment = models.CharField()
    Courses = models.CharField(1000)
    #teacher_name = teacher.Name

