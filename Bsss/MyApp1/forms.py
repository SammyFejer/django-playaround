from django import forms
from django.db.models import Model, QuerySet

from .models import teacher, Assessment



class InputForm(forms.ModelForm):

    class Meta:

        model = teacher

        fields = ['Name', 'Course']
        widgets = {
            'Course': forms.CheckboxSelectMultiple,
            
        }

class Signin(forms.Form):


    entered_email = forms.EmailField(max_length=25)  
    entered_password = forms.CharField(max_length=25)

class teacherAdminForm(forms.ModelForm):
    class Meta:
        model = teacher
        fields = '__all__'

    class Media:
        js = ('admin/js/teacher_admin.js',)

class Assessmentform(forms.ModelForm):

    class Meta:

        model = Assessment

        fields = ['Date', 'weight', 'AssessmentTitle']