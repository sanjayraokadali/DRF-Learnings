from django.shortcuts import render
from rest_framework.response import Response
from users.models import CustomUser
from users.serializers import CustomUserSerializer
from rest_framework.views import APIView
# Create your views here.

class UserView(APIView):

    def get(self,request):

        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data)
