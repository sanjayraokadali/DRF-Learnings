from django.shortcuts import render
from ebooks.models import *
from api.serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser,AllowAny
from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from api.pagination import SmallSetPagination


## USING APIVIEW
class EbookView(APIView):

    def get(self,request):

        ebooks = Ebook.objects.all()

        serializer = EbookSerializer(ebooks, many=True)

        return Response({
            'Ebooks': serializer.data
        })

    def post(self,request):

        serializer = EbookSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response({
                'Ebook Saved': serializer.data
            })
        return Response(serializer.errors)

class EbookDetailView(APIView):

    def get(self,request,pk):

        try:

            ebook = Ebook.objects.get(pk=pk)
            serializer = EbookSerializer(ebook)

            return Response(
                serializer.data,
                status = status.HTTP_200_OK
            )
        except Exception as e:
            return Response(str(e), status= status.HTTP_400_BAD_REQUEST)

class EbookListCreateView(generics.ListCreateAPIView):

    queryset = Ebook.objects.all().order_by('-id')
    serializer_class = EbookSerializer
    pagination_class = SmallSetPagination


class EbookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer

    pagination_class = SmallSetPagination


class ReviewCreateAPIView(generics.CreateAPIView):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


# class EbookListCreateView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#
#     queryset = Ebook.objects.all()
#     serializer_class = EbookSerializer
#
#     def get(self,request, *args, **kwargs):
#
#         return self.list(request,*args, **kwargs)
#
#     def post(self,request, *args, **kwargs):
#
#         return self.create(request,*args, **kwargs)
