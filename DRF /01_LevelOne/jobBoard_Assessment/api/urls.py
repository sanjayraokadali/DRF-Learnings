from django.urls import path
from jobs.models import *
from api.views import *

urlpatterns = [

    path('jobs/', JobListAPI.as_view(), name='job-list-api'),
    path('jobs/<int:pk>/',JobDetailAPI.as_view(),name='job-detail-api'),
]
