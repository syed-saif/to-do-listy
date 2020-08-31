from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

login_ctx = {
        'title':'To-Do Listy-Login/Sign-up',
        'login':True
        }

logout_ctx = {
        'title':'To-Do Listy-Logged out',
        }

urlpatterns = [
    path('', views.home, name='home'),
    path('add', views.add_task, name='add_task'),
    path('login', auth_views.LoginView.as_view(template_name='todolist/login.html', extra_context=login_ctx), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='todolist/logout.html',extra_context=logout_ctx), name='logout'),
    path('sign_up', views.sign_up, name = 'sign_up')
]
