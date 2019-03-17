from django.db import models
from django.contrib.auth.models import User
from accounts_manager.models import Profile
from tinymce import models as tn_models

class Project(models.Model):
    name = models.CharField(max_length=50, blank=False)
    short_description = models.CharField(max_length=100, blank=False, null=True)
    full_description = tn_models.HTMLField(blank=False)
    developers = models.ManyToManyField(Profile,  related_name="Developers")
    author = models.ForeignKey(Profile, related_name="Author",  on_delete=models.PROTECT)

    def __str__(self):
        return self.name

