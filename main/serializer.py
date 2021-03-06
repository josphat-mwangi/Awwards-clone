from rest_framework import serializers
from .models import Project, Rating
from django.contrib.auth.models import User


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'design', 'usability',
                  'content', 'creativity']

class ProjectSerializer(serializers.ModelSerializer):
    rating = RatingSerializer(many=True, read_only=True)
    class Meta :
        model = Project
        fields = ["id", "author", "title", "description", "pub_date",
                  "image", "link",'rating' ]

class UserSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'projects']


