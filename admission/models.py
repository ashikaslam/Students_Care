from django.db import models
from student.models import Student
from teacher.models import Teacher, AvailableTime
# Create your models here.

ADMISSION_STATUS = [
    ('Completed', 'Completed'),
    ('Pending', 'Pending'),
    ('Running', 'Running'),
]
ADMISSION_TYPES = [
    ('Offline', 'Offline'),
    ('Online', 'Online'),
]
class Admission(models.Model):
    student = models.ForeignKey(Student, on_delete = models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete = models.CASCADE)
    admission_types = models.CharField(choices = ADMISSION_TYPES, max_length = 10)
    admission_status = models.CharField(choices = ADMISSION_STATUS, max_length = 10, default = "Pending")
    time = models.ForeignKey(AvailableTime, on_delete = models.CASCADE)
    cancel = models.BooleanField(default = False)
    
    def __str__(self):
        return f"Teacher : {self.teacher.user.first_name} , Student : {self.student.user.first_name}"
    
