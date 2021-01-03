from django.urls import path
from api.views import *
urlpatterns = [

    path('articles/',ArticleAPI.as_view(), name= 'article-api'),
    # path('articles/',article_apiview, name="articles")
    path('articles/<int:pk>/',ArticleDetailAPI.as_view(), name='article-detail')

]
