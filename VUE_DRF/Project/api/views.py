from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import StudentSerializer
from students.models import Student
from rest_framework import generics
from rest_framework import viewsets
# Create your views here.

class StudentAPIView(viewsets.ModelViewSet):

    # def get(self,request):
    #
    #     students = Student.objects.all()
    #
    #     serializer = StudentSerializer(students, many=True)
    #
    #
    #     return Response(serializer.data)

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
