from django.db import models

# Create your models here.

class teacher (models.Model):
    Name = models.CharField(max_length=25)
    Area = models.CharField(max_length=30)
    

   

class course_Area (models.Model):
    #achivement_standment = models.CharField(max_length=30)
    #Courses = models.CharField(max_length=30)
    Teacher = models.ManyToManyField(teacher)

#class cousres (models.Model):
    #Course_Area = models.ForeignKey(course_Area, on_delete=models.CASCADE)
    #courseID = models.IntegerField()


