from django.shortcuts import render
from rest_framework import generics
from quotes.models import Quotes
from api.serializers import QuoteSerializer
from rest_framework.permissions import IsAdminUser,AllowAny
from api.pagination import SmallSet

# Create your views here.
class QuotesListView(generics.ListAPIView):

    permission_classes = [AllowAny,]
    queryset = Quotes.objects.all()
    serializer_class= QuoteSerializer
    pagination_class = SmallSet

class QuoteCreateView(generics.ListCreateAPIView):

    permission_classes = [IsAdminUser,]
    queryset = Quotes.objects.all()
    serializer_class= QuoteSerializer

class QuoteUpdateView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [IsAdminUser,]
    queryset = Quotes.objects.all()
    serializer_class= QuoteSerializer
