
from django.shortcuts import render
from .models import teacher 
from .models import course_Area


# Create your views here.fffgg
def index(request):

   teach = teacher.objects.all()
   CA = course_Area.objects.all()

   '''stuff = {
   'teach' : teaching,
   'CA' : CAing,
   }'''
   return render(request, "MyApp1/index.html", {'content': teach, 'content2': CA})
   

  

