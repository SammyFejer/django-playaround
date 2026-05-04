from django.db import models

# Create your models here.

    

   

class CourseArea(models.Model):
   Title = models.CharField(max_length=25)
   def __str__(self):
        return self.Title


class teacher(models.Model):
    Name = models.CharField(max_length=25)
    Course = models.ManyToManyField(CourseArea)
    def __str__(self):
        return self.Name

    

