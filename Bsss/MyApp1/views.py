
from django.shortcuts import render
from django.http import HttpResponse 
from datetime import datetime
# Create your views here.fffgg
def index (request):
    now = datetime.now()

    return render (
        request,
        "MyApp1/index.html",
        {
            'content' : "<strong>hello Django</stong> on " + now.strftime("%A, %d %B, %Y and %X")
            
        }
        
        
        )

    html_content = "html><head><title>hello Django</title></head><body>"
    html_content = "<strong>heloo Django!</stong> on " + now.strftime("%A, %d %B, %Y and %X")
    html_content ="</body></html>"
    return HttpResponse("hello Django")