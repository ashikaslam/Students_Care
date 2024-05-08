from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.AvailableTime)

class SubjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }

    
admin.site.register(models.Subject, SubjectAdmin)
admin.site.register(models.Teacher)
admin.site.register(models.Review)
