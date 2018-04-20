from django.db import models

# Create your models here.
class Feedback(models.Model):

    Gender = (
        ('남성', 'man'),
        ('여성', 'woman'),
    )
    title = models.CharField(max_length=1000)
    gender = models.CharField(max_length=2, choices=Gender)
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    email = models.EmailField()