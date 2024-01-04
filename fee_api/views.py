from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from fee_api.models import Student
from fee_api.models import StudentSerializers
from django.http import HttpResponse


# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers


# def demo(req):
#     return HttpResponse("hello")