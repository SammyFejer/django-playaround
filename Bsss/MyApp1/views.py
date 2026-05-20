


from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import render, redirect 
from django.urls import reverse
from .models import teacher 
from .models import CourseArea
from .forms import InputForm, Signin

from pypdf import PdfWriter, PdfReader
from reportlab.pdfgen import canvas
from reportlab.platypus import Table
from django.http import FileResponse
from django.contrib.staticfiles.storage import staticfiles_storage
from io import BytesIO  

# Create your views here.fffgg

# Create your views here.fffgg
def index(request):

   teach = teacher.objects.all()
   CA = CourseArea.objects.all()

   return render(request, "MyApp1/index.html", {'content': teach, 'content2': CA})

# def ClassSelect(request):
#     class 
   
def input_view(request):

    if request.method == "POST":

        form = InputForm(request.POST)



        if form.is_valid():

            form.save()

            return redirect("index")

    else:

        form = InputForm()



    return render(request, "MyApp1/input.html", {"form": form})

def SignIn_view(request):

    if request.method == "POST":
        form = Signin(request.POST)

        if form.is_valid():
            
            
                data = form.cleaned_data['entered_email']
                info = teacher.objects.get(Email = data)
                print(form.cleaned_data['entered_email'])
                
                if str(info.Password) == str(form.cleaned_data['entered_password']):
                    teachname = info.id
                    print(teachname)
                    sles = reverse("ClassSelect" , kwargs= {"thingo":teachname})
                    return redirect(sles)
                # else:
                #     bonked = True
                #     return render("MyApp1/SignIn.html",{'bonk': bonked} )
           

            

    else:

        form = Signin()

    return render(request, "MyApp1/SignIn.html", {"form": form})

def classSectect(request, thingo = '1'):
    # teachsname = teacher.objects.get(thingo = id)
    taught = teacher.objects.filter(id = thingo)
    return render(request, "MyApp1/ClassSelect.html", {'content':taught})


def report(request):
    pdf_file = staticfiles_storage.path("unitplanner.pdf")
    try: 
        merger = PdfWriter()

        input1 = PdfReader(generate_pdf())
        input2 = PdfReader(pdf_file, "rb")

        merger.append(input1)
        merger.append(input2)

        buffer = BytesIO()
        merger.write(buffer)
        buffer.seek(0)

        response = FileResponse(buffer, as_attachment=True, filename="attachment.pdf")

    except FileNotFoundError:
        response = FileResponse(generate_pdf(), as_attachment=True, filename = "noAttachment.pdf")
    return response

def generate_pdf():
    buffer = BytesIO()

    p = canvas.Canvas(buffer)

    lines = [('name:', 'Teaching Area:')]
    # hourse =[()]
    teachers = teacher.objects.all()

    for teach in teachers:
        # for Course in teach.Course.all():
        #               hourse.append(teach.Course)

        course_list  = teacher.objects.filter(id = teach.id).values_list("Course__Title", flat=True)
        hehe = ", ".join(course_list)
        lines.append((teach.Name, hehe
                      ))
        # for Course in teach.Course:
        # lines.append((teach.Course.all()))

    table = Table(lines)
    table.wrapOn(p, 300, 300)
    table.drawOn(p,0 ,5)

    p.showPage()
    p.save()

    buffer.seek(0)
    return buffer

   
def input_view(request):

    if request.method == "POST":

        form = InputForm(request.POST)



        if form.is_valid():

            form.save()

            return redirect("index")

    else:

        form = InputForm()



    return render(request, "MyApp1/input.html", {"form": form})