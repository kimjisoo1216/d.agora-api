from django.db import models
import json

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    pwd = models.CharField(max_length=200)


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    tags = models.CharField(max_length=20, default=[])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def set_tags(self, tag):
        self.foo = json.dumps(tag)

    def get_tags(self):
        return json.loads(self.tags)
