from django.shortcuts import render
from ebooks.models import *
from api.serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins

class EbookListCreateView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):

    queryset= Ebook.objects.all()
    serializer_class = EbookSerializer

    def get(self, request, *args, **kwargs):

        return self.list(request, *args, **kwargs)

    def post(self, request,  *args, **kwargs):

        return self.create(request, *args, **kwargs)



# class EbookView(APIView):
#
#     def get(self,request):
#
#         ebooks = Ebook.objects.all()
#
#         serializer = EbookSerializer(ebooks, many=True)
#
#         return Response({
#             'Ebooks': serializer.data
#         })
#
#     def post(self,request):
#
#         serializer = EbookSerializer(data=request.data)
#
#         if serializer.is_valid():
#
#             serializer.save()
#
#             return Response({
#                 'Ebook Saved': serializer.data
#             })
#         return Response(serializer.errors)
