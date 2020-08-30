from django.shortcuts import render
from .models import Tasks

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
    return render(req, 'todolist/login.html', context = ctx)
