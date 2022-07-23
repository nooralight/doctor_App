from django.db import models

# Create your models here.
class User(models.Model):
    fullname = models.TextField(max_length=255)
    password = models.TextField(max_length=255)
    email = models.EmailField(max_length=255)
    isAdmin = models.CharField(default='0' , max_length=2)

def __str__(self):
    return self.full_name