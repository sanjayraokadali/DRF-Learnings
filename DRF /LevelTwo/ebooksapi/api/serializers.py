from rest_framework import serializers
from ebooks.models import *

class ReviewSerializer(serializers.ModelSerializer):

    author = serializers.SerializerMethodField('get_author')
    publication_date = serializers.SerializerMethodField('get_publication_date')


    class Meta:

        model = Review
        fields = '__all__'


    def get_publication_date(self,obj):

        return obj.ebook.publication_date

    def get_author(self,obj):

        return obj.ebook.author


class EbookSerializer(serializers.ModelSerializer):

    reviews = ReviewSerializer(many=True,read_only=True)
    class Meta:

        model = Ebook
        fields = '__all__'
