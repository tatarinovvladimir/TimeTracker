from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User


import os






class Profile(models.Model):
    Custom_User = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    profile_image = models.ImageField(upload_to="avatar", blank=True, null=True, default='avatar/default.jpg')
    date_of_birth = models.DateField(blank=True, null=True)

    user_function = models.CharField(max_length=50)

    def __str__(self):
        return self.Custom_User.username

