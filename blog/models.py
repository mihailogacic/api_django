from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

class Post(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='post_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
