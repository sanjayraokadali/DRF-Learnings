from django.shortcuts import render
from rest_framework import generics
from profiles.models import *
from api.serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet
# Create your views here.

class ProfileView(generics.ListAPIView):

    queryset = Profile.objects.all()
    serializer_class = ProfileSeriailizer
    permission_classes = [IsAdminUser,]


class StatusView(generics.ListAPIView):

    queryset =  ProfileStatus.objects.all()
    serializer_class = StatusSerializer


## CREATING VIEWSETS USING ReadOnlyModelViewSet

# class ProfileViewSet(ModelViewSet):
#
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSeriailizer
#     permission_classes = [IsAdminUser,]

# class StatusViewSet(ModelViewSet):
#     queryset = ProfileStatus.objects.all()
#     serializer_class  = StatusSerializer
#     permission_classes = [AllowAny,]

class ProfileViewSet(mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):

    queryset = Profile.objects.all()
    serializer_class = ProfileSeriailizer
    permission_classes = [IsAdminUser,]


class StatusViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):

    queryset =  ProfileStatus.objects.all()
    serializer_class = StatusSerializer
    permission_classes=[IsAuthenticated,]

    def perform_create(self, serializer):

        user_profile = self.request.user.profile
        serializer.save(user_profile=user_profile)












#
