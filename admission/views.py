from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
# Create your views here.
class AdmissionViewSet(viewsets.ModelViewSet):
    queryset = models.Admission.objects.all()
    serializer_class =  serializers.AdmissionSerializer
    
    
    def get_queryset(self):
        queryset = super().get_queryset() 
        print(self.request.query_params)
        student_id = self.request.query_params.get('student_id')
        if student_id:
            queryset = queryset.filter(student_id=student_id)
        return queryset
