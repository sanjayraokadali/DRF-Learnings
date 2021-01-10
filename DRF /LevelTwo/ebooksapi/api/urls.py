from django.urls import path
from api.views import *



urlpatterns = [

    path('ebooks/',EbookView.as_view(),  name='ebook-api'),
    path('ebooks/<int:pk>/',EbookDetailView.as_view(),name='ebook-detail-api'),

    path('ebooks-generics/',EbookListCreateView.as_view()),
    path('ebooks-details/<int:pk>/',EbookDetailAPIView.as_view()),

    path('review-create/',ReviewCreateAPIView.as_view())
]
