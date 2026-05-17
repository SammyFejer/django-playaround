from django.urls import path
from . import views

urlpatterns = [
    # Uncomment the next line to enable the admin:
    
     path('ClassSelect/<thingo>/', views.classSectect, name = "ClassSelect"),
     path('ClassSelect/', views.classSectect)
     
]



