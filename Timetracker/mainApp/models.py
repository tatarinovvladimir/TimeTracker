from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    project_name = models.CharField(max_length=50, blank=False)
    project_description = models.TextField(blank=False)
    project_developer = models.ManyToManyField(User,  related_name="Developers")
    project_author = models.ForeignKey(User, related_name="Author",  on_delete=models.PROTECT)
