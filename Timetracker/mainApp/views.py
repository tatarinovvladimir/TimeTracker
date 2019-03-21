from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from accounts_manager.models import Profile
from django.contrib.auth.decorators import login_required
from mainApp.forms import uploadProfileImgForm
from mainApp.models import Project
from mainApp.models import Task
from mainApp.models import Comment

import os
from mainApp.forms import TaskEditForm
from mainApp.forms import AddComentForm


@login_required(login_url='/log_in')
def home(request):
    title = "Home"

    user = User.objects.get(username=request.user.username)
    return render(request, 'home/home.html', {"User": user, "title":title})


@login_required(login_url='/log_in')
def auth_logout(request):
    logout(request)
    return HttpResponseRedirect("/log_in")

    
@login_required(login_url='/log_in')
def myprofile(requests):

    user = User.objects.get(username=requests.user.username)
    title = "My profile"

    return render(requests, "myprofile/myprofile.html", { "User": user, "title" : title})


@login_required(login_url='/log_in')
def uploadProfileImg(request):
    print("asdasd")

    if request.method == 'POST':
        print("request is POST")
        form = uploadProfileImgForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            print("sdfdsf")
            user  = User.objects.get(username=request.user.username)
            user.profile.profile_image = form.cleaned_data["avatarimage"]
            user.profile.save()

            return HttpResponseRedirect("myprofile")

        else:
            print("Alarm")
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
        task = Task.objects.filter(project__developers=user.profile)
        task = task.order_by('priority')
        return render(request, "mytasks/mytasks.html", {"User": user, "title" : title, "task" : task})

@login_required(login_url="/log_in")
def journal(request):

        user = User.objects.get(username=request.user.username)
        title = "Journal"
     
        return render(request, "journal/journal.html", { "User": user, "title" : title})

@login_required(login_url="/log_in")
def mytasksdetail(request, pk):
        task = Task.objects.get(id=pk)

        add_comment_form = AddComentForm()
        taskeditform = TaskEditForm()
        comments = Comment.objects.filter(comment_for=task)
        comments = comments.order_by('-date')
        user = User.objects.get(username=request.user.username)
       
        if request.POST and "edittaskname" in request.POST:
            
            taskeditform = TaskEditForm(request.POST, instance=task)
            
            if taskeditform.is_valid():
      
                taskeditform.save()
                return HttpResponseRedirect(request.path)


        elif request.POST and "addcommentname" in request.POST:

            add_comment_form = AddComentForm(request.POST)
            
            if add_comment_form.is_valid():

                add_comment_form = add_comment_form.save(commit=False)
                add_comment_form.commentator = user.profile
                add_comment_form.comment_for = task
                add_comment_form.save()

                return HttpResponseRedirect(request.path)

        elif request.POST and "clearhistoryname" in request.POST:
            print("good")
            comments.delete()
            return HttpResponseRedirect(request.path)

        return render(request, "mytasks/task_template.html", {'task' : task,  "User": user, "taskeditform" : taskeditform, 
            'comments' : comments})
