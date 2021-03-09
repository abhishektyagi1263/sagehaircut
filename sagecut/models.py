from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User,  on_delete=models.DO_NOTHING)

    #additional
    phonenum = models.CharField(max_length=10,)
    def __str__(self):
            return self.user.username

class customer(models.Model):
    first_name = models.CharField(max_length=26)
    email = models.EmailField(max_length=256,unique = True)
    set_date = models.DateField()
    set_time = models.TimeField(auto_now=False, auto_now_add=False,)
