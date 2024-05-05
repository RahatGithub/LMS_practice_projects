from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from . import models 
from .serializers import TeacherSerializer 


class TeacherList(generics.ListCreateAPIView):    
    queryset=models.Teacher.objects.all() 
    serializer_class=TeacherSerializer
    permission_classes=[permissions.IsAuthenticated]
    

class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Teacher.objects.all() 
    serializer_class=TeacherSerializer
    permission_classes=[permissions.IsAuthenticated]


