from django.shortcuts import render
from rest_framework import generics
from profiles.models import *
from api.serializers import *
from rest_framework.permissions import IsAuthenticated,IsAdminUser
# Create your views here.

class ProfileView(generics.ListAPIView):

    queryset = Profile.objects.all()
    serializer_class = ProfileSeriailizer
    permission_classes = [IsAuthenticated,]


class StatusView(generics.ListAPIView):

    queryset =  ProfileStatus.objects.all()
    serializer_class = StatusSerializer
