from django.urls import path
from api.views import *



urlpatterns = [

    path('ebooks/',EbookListCreateView.as_view(),  name='ebook-api'),
]
