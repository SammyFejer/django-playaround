
from django.shortcuts import render, redirect
from .models import teacher 
from .models import course_Area
from .forms import InputForm


# Create your views here.fffgg
def index(request):

   teach = teacher.objects.all()
   CA = course_Area.objects

   '''stuff = {
   'teach' : teaching,
   'CA' : CAing,
   }'''
   return render(request, "MyApp1/index.html", {'content': teach, 'content2': CA})
   
def input_view(request):

    if request.method == "POST":

        form = InputForm(request.POST)



        if form.is_valid():

            form.save()

            return redirect("index")

    else:

        form = InputForm()



    return render(request, "MyApp1/input.html", {"form": form})
  

