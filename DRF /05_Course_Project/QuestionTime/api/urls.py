from django.urls import path,include

from api.views import QuestionViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('questions', QuestionViewSet)

urlpatterns =[

    path('',include(router.urls))

]
