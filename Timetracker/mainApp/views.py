from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from accounts_manager.models import Profile
from django.contrib.auth.decorators import login_required
from mainApp.forms import uploadProfileImgForm
from mainApp.models import Project
from mainApp.models import Task
from mainApp.models import NewsPost
from mainApp.models import Comment
from mainApp.models import JournalPost
from mainApp.forms import TaskEditForm
from mainApp.forms import TaskAddForm
from mainApp.forms import AddComentForm
from mainApp.forms import AddNoteForm

from django.core.mail import send_mail
from django.conf import settings
import os



@login_required(login_url='/log_in')
def home(request):
    title = "Home"
    news = NewsPost.objects.filter().order_by('-date')[:20]
    user = User.objects.get(username=request.user.username)
    return render(request, 'home/home.html', {"User" : user, "title" : title, "news" : news})


@login_required(login_url='/log_in')
def auth_logout(request):
    logout(request)
    return HttpResponseRedirect("/log_in")

    
@login_required(login_url='/log_in')
def myprofile(requests):
    chief_admin_group = Group.objects.filter(name="Chief Administrator")
    admin_group = Group.objects.filter(name="Administrator")
    moder_group = Group.objects.filter(name="Moderator")
    user = User.objects.get(username=requests.user.username)
    title = "My profile"

    return render(requests, "myprofile/myprofile.html", { "User": user, "title" : title,
     "chief_admin_group" : chief_admin_group, "admin_group":admin_group, "moder_group":moder_group})


@login_required(login_url='/log_in')
def uploadProfileImg(request):
    print("asdasd")

    if request.method == 'POST':

        form = uploadProfileImgForm(data=request.POST, files=request.FILES)

        if form.is_valid():

            user  = User.objects.get(username=request.user.username)
            user.profile.profile_image = form.cleaned_data["avatarimage"]
            user.profile.save()

            return HttpResponseRedirect("myprofile")

        else:

            print(form.errors)

    return HttpResponseRedirect("myprofile")

@login_required(login_url="/log_in")
def myprojects(request):


        user = User.objects.get(username=request.user.username)
        title = "My projects"
        project = Project.objects.filter(developers=user.profile)


        return render(request, "myprojects/myprojects.html", { "User": user, "title" : title, "project":project})

@login_required(login_url="/log_in")
def mytasks(request):

        user = User.objects.get(username=request.user.username)
        title = "My tasks"
        task = Task.objects.filter(implementers=user.profile).order_by('priority')
        addform = TaskAddForm()


        if request.POST:
            addform = TaskAddForm(request.POST)
            print("post")

            if addform.is_valid():
                print("valid")

                newaddform = addform.save(commit=False)
                
                newaddform.creator = user.profile
                newaddform.save()
                addform.save_m2m()
                
                print(addform)
                

                return HttpResponseRedirect(request.path)
            else:
                return HttpResponseRedirect(request.path)

        return render(request, "mytasks/mytasks.html", {"User": user, "title" : title, "task" : task, 'addform' : addform})

@login_required(login_url="/log_in")
def journal(request):

        user = User.objects.get(username=request.user.username)
        title = "Journal"
        journalpost = JournalPost.objects.filter(for_task__implementers=user.profile).order_by('-post_date')[:50]
        addnoteform = AddNoteForm()
       
        addnoteform.fields["for_task"].queryset = Task.objects.filter(project__developers=user.profile)

        if request.POST:

            addnoteform = AddNoteForm(request.POST)
            if addnoteform.is_valid():

                addnoteform = addnoteform.save(commit=False)
                addnoteform.made_by = user.profile
                addnoteform.save()
                
                return HttpResponseRedirect(request.path)
       
        return render(request, "journal/journal.html", { "User": user, "title" : title, "journalpost" : journalpost,
         'addnoteform' : addnoteform})

@login_required(login_url="/log_in")
def mytasksdetail(request, pk):
        task = Task.objects.get(id=pk)
        old_task = Task.objects.get(id=pk)
        add_comment_form = AddComentForm()
        taskeditform = TaskEditForm()
        chief_admin_group = Group.objects.filter(name="Chief Administrator")
        admin_group = Group.objects.filter(name="Administrator")
        moder_group = Group.objects.filter(name="Moderator")
        comments = Comment.objects.filter(comment_for=task).order_by('-date')
        journal = JournalPost.objects.filter(for_task=task)
        hours = 0
        for i in journal:
            hours += i.used_time


        user = User.objects.get(username=request.user.username)
       
        if request.POST and "edittaskname" in request.POST:
            
            taskeditform = TaskEditForm(request.POST, instance=task)
            
            if taskeditform.is_valid():
                
                subject = '{} was changed!'.format(task)
                message = '''Hello! \n We have a few changes in {}. Please check it! \n \nList of changes: \n \n'''.format(old_task)

                email_from = settings.EMAIL_HOST_USER
                recipient_list = []

                for i in task.project.developers.all():
                    recipient_list.append(i.Custom_User.email)
                message += "Old fields: \n"
                for i in taskeditform.changed_data:
                    message += "{} - {} \n".format(i, getattr(old_task,i))

                message += "\nNew fields: \n"
                for i in taskeditform.changed_data:
                    message += "{} - {} \n".format(i, getattr(task,i)) 

                message += "\n Task changed by {} {}".format(user.first_name, user.last_name)
                taskeditform.save()
                send_mail( subject, message, email_from, recipient_list )
                return HttpResponseRedirect(request.path)


        elif request.POST and "addcommentname" in request.POST:

            add_comment_form = AddComentForm(request.POST)
            print("post")
            if add_comment_form.is_valid():
                print("valid")
                add_comment_form = add_comment_form.save(commit=False)
                add_comment_form.commentator = user.profile
                add_comment_form.comment_for = task
                add_comment_form.save()

                return HttpResponseRedirect(request.path)
            else:
                print("not valid")

        elif request.POST and "clearhistoryname" in request.POST:
            print("good")
            comments.delete()
            return HttpResponseRedirect(request.path)

        return render(request, "mytasks/task_template.html", {'task' : task,  "User": user, "taskeditform" : taskeditform, 
            'comments' : comments, "chief_admin_group" : chief_admin_group, "admin_group":admin_group, "moder_group":moder_group,
            'hours' : hours})
