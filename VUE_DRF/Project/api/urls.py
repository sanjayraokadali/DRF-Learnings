from django.urls import path,include
from api.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r"students", StudentAPIView)

urlpatterns = [

    # path('student-list/',StudentAPIView.as_view(),name="student-list"),
    path('',include(router.urls))
]
