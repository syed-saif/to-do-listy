from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(req):
    d = {'title':'my title'}
    return render(req, 'todolist/home.html', context = d)

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
