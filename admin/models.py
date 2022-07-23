from django.db import models

# Create your models here.

class Doctor(models.Model):
    doctor_name = models.TextField(max_length=255)
    sector = models.TextField(max_length=255)
    available = models.CharField(max_length=10,default='a')

def __str__(self):
    return self.doctor_name