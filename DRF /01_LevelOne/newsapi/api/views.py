# from django.shortcuts import render
from rest_framework.views import APIView
from news.models import Article
from api.serializers import ArticleSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.generics import get_object_or_404

# Create your views here.
class ArticleAPI(APIView):

    def get(self, request):

        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)

        return Response({

            'Articles': serializer.data,
        })

    def post(self,request):

        serializer = ArticleSerializer(data = request.data)

        if serializer.is_valid():

            serializer.save()

            return Response({

                'Article': serializer.data
            })
        return Response(serializer.errors)

class ArticleDetailAPI(APIView):

    def get_object(self,pk):

        article = get_object_or_404(Article, pk=pk)

        return article

    def get(self,request,pk):

        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def delete(self,request,pk):

        article = self.get_object(pk)
        article.delete()
        return Response({
            'status':status.HTTP_204_NO_CONTENT,
            'message': 'Article deleted!'

        })





# @api_view(['GET','POST'])
# def article_apiview(request):
#
#     if request.method == 'GET':
#
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles,many=True)
#
#         return Response({
#             'Articles': serializer.data,
#             'status': status.HTTP_200_OK
#         })
#
#     elif request.method == 'POST':
#
#         serializer = ArticleSerializer(data = request.data)
#
#         if serializer.is_valid():
#
#             serializer.save()
#
#             return Response({
#                 'status': status.HTTP_201_CREATED,
#                 'articles' : serializer.data
#                             })
#         else:
#
#             return Response({
#                 'status': status.HTTP_400_BAD_REQUEST
#             })
