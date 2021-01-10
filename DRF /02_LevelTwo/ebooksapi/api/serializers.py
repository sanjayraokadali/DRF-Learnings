from rest_framework import serializers
from ebooks.models import *
from rest_framework.generics import get_object_or_404

class ReviewSerializer(serializers.ModelSerializer):


    class Meta:

        model = Review
        fields = '__all__'

class EbookSerializer(serializers.ModelSerializer):

    class Meta:

        model = Ebook
        fields = '__all__'

    reviews = ReviewSerializer(many=True,read_only=True)
