from django.contrib import admin
from .models import teacher 
from .models import CourseArea 
from .models import subCourse
from .models import Unit
from .models import Assessment

class teacherAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.Course__courseArea__course == "Course":
            kwargs["queryset"] = CourseArea.objects.filter()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

# Register your models here.
admin.site.register(teacher)
admin.site.register(CourseArea)
admin.site.register(subCourse)
admin.site.register(Unit)
admin.site.register(Assessment)
#kjlfdskldff