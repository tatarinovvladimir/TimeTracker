from django import forms
from django.contrib.auth.models import User
from mainApp.models import Task

class uploadProfileImgForm(forms.Form):
	avatarimage = forms.ImageField()


class TaskEditForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ['topic','description','start_date','end_date','task_type','priority','estimated_time','project']

	

