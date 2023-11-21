from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class Post(models.Model):
    title = models.CharField( max_length=50)
    body = models.TextField(max_length=500)
    create_date = models.DateField(auto_now_add=True)
    last_update_date = models.DateField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField(max_length=250)
    create_date = models.DateField(auto_now_add=True)
    author =models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.body