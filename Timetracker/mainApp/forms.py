from django import forms
from django.contrib.auth.models import User
from mainApp.models import Task
from mainApp.models import Comment
from mainApp.models import JournalPost
from mainApp.models import Project

class uploadProfileImgForm(forms.Form):
    avatarimage = forms.ImageField()


class TaskEditForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['topic','description','start_date','end_date','task_type','priority','estimated_time','project']
        exclude = ['implementers']


class AddComentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comm_text']
        exclude = ['commentator', 'comment_for']

class AddNoteForm(forms.ModelForm):
    class Meta:
        model = JournalPost
        fields = ["used_time", "post_text", "for_task"]
        exclude = ['post_date', 'made_by']


class TaskAddForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['topic','description', 'implementers', 'start_date','end_date','task_type','priority','estimated_time','project']
        exclude = ['creator']



