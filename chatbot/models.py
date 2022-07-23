from django.db import models

# Create your models here.

class Appointment(models.Model):
    user_id = models.TextField(max_length=25)
    doctor_name = models.TextField(max_length=255)
    app_date = models.DateField()
    time_book = models.TextField(max_length=25)