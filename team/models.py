from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=100, unique=True, error_messages={'unique':"Email already used!"})
    phone = models.CharField(max_length=50, blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
    

    class Meta:
        db_table = 'team_user'
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ["-id"]
        
    def __str__(self):
        return self.email



class Team(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    
    
    def __str__(self):
        return self.name
    
    