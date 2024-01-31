from django.db import models


# Create your models here.
class table(models.Model):
    firstname=models.CharField(max_length=200,null=True)
    lastname=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    phone=models.IntegerField()
    password=models.CharField(max_length=200,null=True)
    
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)