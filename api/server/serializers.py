# from django.contrib.auth.models import User, Group
from api.server.models import User, Post, Comment, Major, Tag
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    like_users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    like_users = UserSerializer(many=True, read_only=True)
    major = serializers.ReadOnlyField(source='major.name')

    class Meta:
        model = Post
        fields = '__all__'
