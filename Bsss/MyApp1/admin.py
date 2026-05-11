from django.contrib import admin
from .models import teacher 
from .models import CourseArea 
from .models import subCourse
from .models import Unit
from .models import Assessment

#class teacherAdmin(admin.ModelAdmin):
#    def formfield_for_foreignkey(self, db_field, request, **kwargs):
#        if db_field.Course__courseArea__course == "Course":
#            kwargs["queryset"] = CourseArea.objects.filter()
#        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class teacherAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Course', 'classes']
    list_filter = ['Course', 'classes']

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if request.method == 'GET':
            Course_id = request.Get.get('Course__id')
            if Course_id:
                form.base_fields["classes"].queryset = Unit.objects.filter(Course_id=Course_id)
            else:
                form.base_fields["classes"].queryset = Unit.objects.none() # this returns an empty queryset if no brand is selected
        return form


# Register your models here.d
admin.site.register(teacher, teacherAdmin)
admin.site.register(CourseArea)
admin.site.register(subCourse)
admin.site.register(Unit)
admin.site.register(Assessment)
#kjlfdskldff