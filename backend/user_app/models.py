from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core import validators as v

# Create your models here.
class App_user(AbstractUser): 
    username = models.EmailField(verbose_name='email address', unique=True) #made username equal the email field (somehow when i createsuperuser it needs username)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []