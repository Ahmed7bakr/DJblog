from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User,related_name='post_user',on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=5000)
    activate = models.BooleanField(default=False)
    image = models.ImageField(upload_to='posts/')

    def __str__(self):
        return self.title