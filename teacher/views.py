from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework import filters, pagination


class SubjectViewset(viewsets.ModelViewSet):
    queryset = models.Subject.objects.all()
    serializer_class = serializers.SubjectSerializer

    

class AvailableTimeForSpecificTeacher(filters.BaseFilterBackend):
    def filter_queryset(self, request, query_set, view):
        teacher_id = request.query_params.get("teacher_id")
        if teacher_id:
            return query_set.filter(teacher = teacher_id)
        return query_set

class AvailableTimeViewset(viewsets.ModelViewSet):
    queryset = models.AvailableTime.objects.all()
    serializer_class = serializers.AvailableTimeSerializer
    filter_backends = [AvailableTimeForSpecificTeacher]

class TeacherPagination(pagination.PageNumberPagination):
    page_size = 2 # items per page
    page_size_query_param = page_size
    max_page_size = 100

class TeacherViewset(viewsets.ModelViewSet):
    queryset = models.Teacher.objects.all()
    serializer_class = serializers.TeacherSerializer
    filter_backends = [filters.SearchFilter]
    pagination_class = TeacherPagination
    search_fields = ['user__first_name', 'user__email', 'subject__name']
    
class ReviewViewset(viewsets.ModelViewSet):
    
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer