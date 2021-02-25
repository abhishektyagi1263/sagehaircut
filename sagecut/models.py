from django.db import models

# Create your models here.
class reservations(models.Model):
    fullname =  models.CharField(max_length=26)
    phonenum =  models.CharField(max_length=10,unique=True)
    setdat = models.DateField()
    settime =  models.TimeField(auto_now=False, auto_now_add=False)
