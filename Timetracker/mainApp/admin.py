from django.contrib import admin
from mainApp.models import Project
from mainApp.models import Task
from mainApp.models import Comment

admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Comment)

