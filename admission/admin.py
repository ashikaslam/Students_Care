from django.contrib import admin
from . import models

# Register your models here.

class AdmissionAdmin(admin.ModelAdmin):
    list_display = ['teacher_name', 'student_name', 'admission_types', 'admission_status', 'time', 'cancel']
    def student_name(self,obj):
        return obj.student.user.first_name
    
    def teacher_name(self,obj):
        return obj.teacher.user.first_name
    
    
admin.site.register(models.Admission, AdmissionAdmin)
