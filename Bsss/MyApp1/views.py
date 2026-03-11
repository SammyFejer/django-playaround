
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import teacher 
from .models import course_Area


# Create your views here.fffgg
def index(request):

   teach = teacher.objects.all(),
   CA = course_Area.objects.all(),

   stuff = {
   'teach' : teach,
   'CA' : CA,
   }
   return render(request, "MyApp1/index.html", {'content': stuff})
   

  

