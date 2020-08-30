from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Tasks
from .forms import UserRegisterForm

# Create your views here.
from django.http import HttpResponse


def home(req, **kwargs):
    view_ct = req.GET.get('view', None)
    if view_ct:
        tasks = Tasks.objects.filter(completed=True)
    else:
        tasks = Tasks.objects.filter(completed=False)
    ctx = {
            'title':'To-Do Listy-Home',
            'tasks':tasks,
            'view':view_ct
        }
    return render(req, 'todolist/home.html', context = ctx)

def login(req):
    ctx = {'title':'To-Do Listy-Login/Sign-up',
            'login':True
    }
    return render(req, 'todolist/login.html', context = ctx)

def sign_up(req):
    ctx = {'title':'To-Do Listy-Login/Sign-up',
            'login':False
    }
    if req.method == 'POST':
        form = UserRegisterForm(req.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(req, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    ctx['form'] = form
    return render(req, 'todolist/login.html', context = ctx)
