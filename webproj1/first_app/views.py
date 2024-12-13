from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from django.contrib.auth.views import LoginView,LogoutView
from .forms import login
# Create your views here.
def view_airport(req:HttpRequest)-> HttpResponse:
    return HttpResponse("Hello!")
def view_home(req:HttpRequest) -> HttpResponse:
    return render(req,template_name="home.html")
def view_login(req:HttpRequest)->HttpResponse:
    login_render=LoginView.as_view(
        template_name='login.html',
        authentication_form=login,
        extra_context={
            'title':'Вход в систему',
            #'form':login
        }
    )
    return login_render(req)