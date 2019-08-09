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
    like_posts = models.ManyToManyField(
        'Post',  blank=True)
    like_comments = models.ManyToManyField(
        'Comment',  blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(default="")
    major = models.ForeignKey(
        'Major', on_delete=models.CASCADE, blank=True, null=True)
    tags = models.ForeignKey(
        'Tag', on_delete=models.CASCADE, blank=True, null=True)
    author = models.ForeignKey(
        'User', default="", on_delete=models.CASCADE, related_name="posts")
    like_users = models.ManyToManyField(
        'User', blank=True)
    view_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        'Post', default="", on_delete=models.CASCADE, related_name="comments", null=True, blank=True)
    author = models.ForeignKey(
        'User', default="", on_delete=models.CASCADE, related_name="comments")
    content = models.TextField(default="")
    like_users = models.ManyToManyField(
        'User',  blank=True)
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
