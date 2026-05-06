from django.db import models

# Create your models here.

    

   

class CourseArea(models.Model):
   Title = models.CharField(max_length=25)
   def __str__(self):
        return self.Title




class subCourse(models.Model):
    coursearea = models.ForeignKey(CourseArea, on_delete=models.CASCADE)
    courseTitle = models.CharField(max_length=25)
    
    
    def __str__(self):
        return self.courseTitle

class Unit(models.Model):
    UnitName = models.CharField(max_length=25)
    course = models.ForeignKey(subCourse, on_delete=models.CASCADE)
    Accreditation = models.CharField(max_length=25)
    UnitDescription = models.CharField(max_length=1000)
    UnitGoals = models.CharField(max_length=1000)
    ContentDescriptions =models.CharField(max_length=1000)
    def __str__(self):
        return self.UnitName

class Assessment(models.Model):
    Date = models.DateField()
    weight = models.CharField(max_length=25)
    AssessmentTitle = models.CharField(max_length=25)
    AssessmentUnit = models.ForeignKey(Unit, on_delete=models.CASCADE)

def InCourseArea():
    for course in subCourse 
    return 
# g
class teacher(models.Model):
    Name = models.CharField(max_length=25)
    Course = models.ManyToManyField(CourseArea)
    Email = models.CharField(max_length=25)
    Password = models.CharField(max_length=25)
    classes = models.ManyToManyField.limit_choices_to(Unit, InCourseArea)
    def __str__(self):
        return self.Name        