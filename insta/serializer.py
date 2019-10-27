from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Image

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_photo', 'user')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('image','image_name', 'image_caption', 'link','comment')