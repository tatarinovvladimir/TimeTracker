from django import forms
from django.contrib.auth.models import User
from mainApp.models import Task
from mainApp.models import Comment


class uploadProfileImgForm(forms.Form):
    avatarimage = forms.ImageField()


class TaskEditForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['topic','description','start_date','end_date','task_type','priority','estimated_time','project']

class AddComentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comm_text']
        exclude = ['commentator', 'comment_for']



