from django.urls import path,include

from api.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('questions', QuestionViewSet)

urlpatterns =[

    path('',include(router.urls)),
    path('questions/<slug:slug>/answer/',AnswerAPIView.as_view(), name='create-answer'),
    path('questions/<slug:slug>/answerlist/',AnswerListAPIView.as_view(), name='answer-list'),
    path('answers/<int:pk>/',AnswerRUDAPIView.as_view(), name='answer-detail'),
    path('answers/<int:pk>/like/',AnswerLikeAPIView.as_view(),name='answer-like'),



]
