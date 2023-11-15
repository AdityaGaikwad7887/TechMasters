from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import User

import uuid

class ProductImage(models.Model):
    image = models.ImageField(upload_to="img/%y")
    caption = models.CharField(max_length=20 , null=False)
    charges = models.IntegerField(null=False)

    def __str__(self):
        return self.caption
    
class ServiceImage(models.Model):
    image = models.ImageField(upload_to="img/%y")
    caption = models.CharField(max_length=20 , null=False)
    charges = models.IntegerField(null=False)

    def __str__(self):
        return self.caption

class LabourUser(models.Model):
    username = models.CharField(max_length=50 , null = False,unique=True)
    email = models.EmailField(null=False)
    userId = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    password = models.CharField(max_length=10 , null = False)
    profession = models.CharField(max_length=10 , null = False)
    location = models.CharField(max_length=10 , null = False)
    image = models.ImageField(upload_to="img/%y",default="../media/defualtuser.jpg")
    mobile = models.PositiveIntegerField(null=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    score = models.IntegerField(default=0 ,null=True)
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
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)


    def __str__(self):
        return self.username
        
    def save(self, *args,**kwargs):
        self.password = User.objects.make_random_password()
        return super().save(*args,**kwargs)


class quiz(models.Model):
    service  = models.CharField(max_length=50)

    def get_question(self):
        return self.question_set.all()
    
    def __str__(self):
        return self.service


class questions(models.Model):
    text = models.CharField(max_length=200)
    quiz = models.ForeignKey(quiz,on_delete=models.CASCADE)

    def __str__(self):
        return self.text
    
    def get_answer(self):
        return self.answer_set.all()
    

class Answer(models.Model):
    text = models.CharField(max_length=200)
    correct  = models.BooleanField(default=False)
    questions = models.ForeignKey(questions,on_delete=models.CASCADE)

    def __str__(self):
        return self.text 