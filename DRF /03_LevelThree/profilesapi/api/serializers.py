from rest_framework import serializers
from profiles.models import *


class ProfileSeriailizer(serializers.ModelSerializer):

    user = serializers.StringRelatedField()

    class Meta:

        model = Profile
        fields = '__all__'

class StatusSerializer(serializers.ModelSerializer):

    def get_user_profile(self,obj):

        user_profile = obj.user_profile.user.username
        return user_profile

    user_profile = serializers.SerializerMethodField('get_user_profile')

    class Meta:

        model = ProfileStatus
        fields = '__all__'
