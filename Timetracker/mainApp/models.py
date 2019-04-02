from django.db import models
from django.contrib.auth.models import User
from accounts_manager.models import Profile
from tinymce import models as tn_models
import  datetime as dt
class Project(models.Model):
    name = models.CharField(max_length=50, blank=False)
    short_description = models.CharField(max_length=100, blank=False, null=True)
    full_description = tn_models.HTMLField(blank=False)
    developers = models.ManyToManyField(Profile,  related_name="Developers")
    author = models.ForeignKey(Profile, related_name="Author",  on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class NewsPost(models.Model):
    name = models.CharField(max_length=50, blank=False)
    text = tn_models.HTMLField(blank=False)
    sender = models.ForeignKey(Profile,  on_delete=models.CASCADE)
    date = models.DateTimeField(default=dt.datetime.now, blank=False)
    limitation_time = models.IntegerField(verbose_name="Actual time for post (in days)", blank=True, null=True)

    def __str__(self):
        return self.name

class Task(models.Model):

    topic = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=False, max_length=400)
    start_date = models.DateField(blank=False )
    end_date = models.DateField(blank=False)
    task_type = models.CharField(max_length=50, blank=False, choices=(('Bug', 'Bug'), ('Feature', 'Feature')) )
    priority = models.CharField(max_length=50,choices=(("Normal", "Normal"),("High", "High"),("Extra", "Extra")))
    estimated_time = models.FloatField(verbose_name="Estimated time in hours", blank=False)
    implementers = models.ManyToManyField(Profile, related_name="implementers")
    creator = models.ForeignKey(Profile,  null=True, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, related_name="project", on_delete=models.CASCADE)




    def __str__(self):
        return self.topic

class Comment(models.Model):
    comment_for = models.ForeignKey(Task, on_delete=models.CASCADE, null=True)
    commentator = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL)
    comm_text = models.TextField(max_length=500, blank=False)
    date = models.DateTimeField(default=dt.datetime.now, blank=False)

    def __str__(self):
        return str(self.commentator) + " comment for " + str(self.comment_for)

class JournalPost(models.Model):
    post_date = models.DateTimeField(default=dt.datetime.now, blank=False)
    used_time = models.FloatField(blank=False, null=True)
    post_text = models.TextField(blank=False, max_length=400)
    for_task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True)
    made_by = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.made_by) + " journal post"