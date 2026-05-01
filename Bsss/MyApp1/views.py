
from urllib import response
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import render, redirect
from .models import teacher 
from .models import course_Area
from .forms import InputForm
from pypdf import PdfWriter, PdfReader
from reportlab.pdfgen import canvas
from reportlab.platypus import Table
from django.http import FileResponse
from django.contrib.staticfiles.storage import staticfiles_storage
from io import BytesIO  

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

    teachers = teacher.objects.all()

    for teach in teachers:
        lines.append((teach.Name))
        for Course in teach.Course.all():
            lines.append((Course.Title))

    table = Table(lines)
    table.wrapOn(p, 300, 300)
    table.drawOn(p,0 ,5)

    p.showPage()
    p.save()

    buffer.seek(0)
    return buffer

