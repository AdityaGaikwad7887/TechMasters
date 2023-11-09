from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
import uuid
# Create your models here.

# class LabourUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user


class LabourUser(models.Model):
    username = models.CharField(max_length=50 , null = False,unique=True)
    email = models.EmailField(null=False)
    userId = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    password = models.CharField(max_length=10 , null = False)
    profession = models.CharField(max_length=10 , null = False)
    location = models.CharField(max_length=10 , null = False)
    mobile = models.IntegerField(null=False)
    # excperience = models.IntegerField(default=0)
    skills = models.CharField(max_length=50 , null=False,default="No skills")

    # objects = LabourUserManager()

    USERNAME_FIELD = 'userId'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def save(self, *args,**kwargs):
        self.password = User.objects.make_random_password()
        return super().save(*args,**kwargs)

class NormalUser(models.Model):
    username = models.CharField(max_length=50 , null = False ,unique=True)
    email = models.EmailField(null=False)
    password = models.CharField(max_length=10 , null = False) 
    location = models.CharField(max_length=10 , null = False)
    mobile = models.IntegerField(null=False)   


    def __str__(self):
        return self.username
        
    def save(self, *args,**kwargs):
        self.password = User.objects.make_random_password()
        return super().save(*args,**kwargs)

