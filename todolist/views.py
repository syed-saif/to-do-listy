from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Tasks
from .forms import UserRegisterForm

# Create your views here.
from django.http import HttpResponse

#a helper function that returns the task_set for a given user
def getTaskSet(user, view_ct):
    tasks = user.tasks_set.all()
    if view_ct:
        tasks = tasks.filter(completed=True)
    else:
        tasks = tasks.filter(completed=False)
    return tasks

@login_required
def home(req):
    user = req.user
    view_ct = req.GET.get('view', None)
    tasks = getTaskSet(user, view_ct)
    ctx = {
            'title':'To-Do Listy-Home',
            'tasks':tasks,
            'view':view_ct
        }
    return render(req, 'todolist/home.html', context = ctx)

@login_required
def add_task(req):
    user = req.user
    view_ct = req.GET.get('view', None)
    tasks = getTaskSet(user, view_ct)
    ctx = {
            'title':'To-Do Listy-Add Task',
            'view':view_ct,
            'tasks':tasks
        }
    if req.method == 'POST':
        title, body = req.POST.get('title'), req.POST.get('content')
        new_task = user.tasks_set.create(title=title, body=body)
        new_task.save()
        messages.success(req, 'Task added successfully!')
        return redirect('home')
    else:
        return render(req, 'todolist/add.html', context=ctx)

def sign_up(req):
    ctx = {
            'title':'To-Do Listy-Login/Sign-up',
            'login':False
        }
    if req.method == 'POST':
        form = UserRegisterForm(req.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(req, f'Account created for {username}! Now you can Log In:')
            return redirect('login')
    else:
        form = UserRegisterForm()
    ctx['form'] = form
    return render(req, 'todolist/login.html', context = ctx)
