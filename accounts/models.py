from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    username=models.CharField(max_length=200,null=True,blank=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    location = models.CharField(max_length=300,null=True,blank=True)
    email=models.EmailField()
    profile_image=models.ImageField(default="profile/images/user-default.png",upload_to='profile/images',null=True,blank=True)
    bio=models.TextField(null=True,blank=True)

    def __str__(self):
        return  self.username
