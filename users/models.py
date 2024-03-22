from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
  avatar = models.ImageField(upload_to='users_images', blank=True, null=True)
