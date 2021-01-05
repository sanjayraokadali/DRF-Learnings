from rest_framework import serializers
from jobs.models import jobOffer

class JobSerializer(serializers.ModelSerializer):

    class Meta:

        model = jobOffer
        fields = '__all__'

        
