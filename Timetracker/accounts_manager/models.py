from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
import os





class Profile(models.Model):
    Custom_User = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to="avatar", blank=True, null=True)

    date_of_birth = models.DateField(blank=True, null=True)
    user_function = models.CharField(max_length=50)

