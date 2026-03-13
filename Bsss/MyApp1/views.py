
from django.shortcuts import render
from .models import teacher 
from .models import course_Area


# Create your views here.fffgg
def index(request):

   teaching = teacher.objects.all(),
   CAing = course_Area.objects.all(),

   stuff = {
   'teach' : teaching,
   'CA' : CAing,
   }
   return render(request, "MyApp1/index.html", {'content': stuff})
   

  

