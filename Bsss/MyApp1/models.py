from django.db import models

# Create your models here.

    

   

class CourseArea(models.Model):
   Title = models.CharField(max_length=25)


class teacher(models.Model):
    Name = models.CharField(max_length=25)
    Course = models.ManyToManyField(CourseArea)