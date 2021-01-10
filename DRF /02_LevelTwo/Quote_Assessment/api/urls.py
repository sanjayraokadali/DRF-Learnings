from django.urls import path
from api.views import *

urlpatterns = [

    path('quote-list',QuotesListView.as_view()),
    path('quote-create/',QuoteCreateView.as_view()),
    path('quote-retrieve/<int:pk>',QuoteUpdateView.as_view()),
]
