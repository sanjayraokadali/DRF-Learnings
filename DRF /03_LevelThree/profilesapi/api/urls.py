from django.urls import path
from api.views import *


urlpatterns = [

    path('profiles/',ProfileView.as_view()),
    path('statuses/',StatusView.as_view()),
]
