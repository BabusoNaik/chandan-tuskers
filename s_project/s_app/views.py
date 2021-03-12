from django.shortcuts import render
from django.http import HttpResponse
# from s_app.models import User
from s_app.forms import NewUser
from . import forms

# Create your views here.
def thanku(request):

    return render(request,'s_app/thanku.html')



def squad(request):

    return render(request,'s_app/squad.html')


def about(request):

    return render(request,'s_app/about.html')



def index(request):

    return render(request,'s_app/index.html')


def users(request):


    form = NewUser()

    if request.method=='POST':
        form = NewUser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return thanku(request)

        else:
            print("INVALID FORM")

    return render(request,'s_app/users.html',{'form':form})
