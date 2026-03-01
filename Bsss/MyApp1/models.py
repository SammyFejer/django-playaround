from django.db import models

# Create your models here.

class teacher (models.Model):
    Name = models.CharField(max_length=25)
    Area = models.CharField(max_length=30)
    #course_Area = models.

   

class course_Area (models.Model):
    Achivement_standment = models.CharField(max_length=30)
    Courses = models.CharField(max_length=30)
    Teacher = models.ManyToManyField(teacher)

