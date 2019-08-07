from django.db import models
from django.contrib.auth.models import User
import json

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    pwd = models.CharField(max_length=20)
    profile_img = models.ImageField(blank=True)
    major = models.ForeignKey(
        'Major', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(default="")
    comments = models.ForeignKey(
        'Comment', default="", on_delete=models.CASCADE, related_name="post_comments", null=True)
    tags = models.ForeignKey(
        'Tag', on_delete=models.CASCADE, blank=True, null=True)
    major = models.ForeignKey(
        'Major', on_delete=models.CASCADE, blank=True, null=True)
    author = models.ForeignKey(
        'User', default="", on_delete=models.CASCADE, related_name="post_author")
    like_users = models.ForeignKey(
        'User', default="", blank=True, null=True, on_delete=models.CASCADE, related_name="post_like_users")
    view_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField(default="")
    author = models.ForeignKey(
        'User', default="", on_delete=models.CASCADE, related_name="comment_author")
    like_users = models.ForeignKey(
        'User', default="", blank=True, null=True, on_delete=models.CASCADE, related_name="comment_like_users")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content


class Major(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
