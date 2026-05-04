from django import forms
from django.db.models import QuerySet

from .models import teacher



class InputForm(forms.ModelForm):

    class Meta:

        model = teacher

        fields = ['Name', 'Course']
        widgets = {
            'Course': forms.CheckboxSelectMultiple,
            
        }
