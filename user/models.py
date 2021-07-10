from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    # email = models.EmailField()
    image= models.ImageField(upload_to='image',default='red_flower.jpg')

    def __str__(self):
        return self.user.username
