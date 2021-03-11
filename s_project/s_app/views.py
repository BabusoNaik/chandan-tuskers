from django.shortcuts import render
from django.http import HttpResponse
# from s_app.models import User
from s_app.forms import NewUser
from . import forms

# Create your views here.

def index(request):

    return render(request,'s_app/index.html')


def users(request):


    form = NewUser()

    if request.method=='POST':
        form = NewUser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:
            print("INVALID FORM")

    return render(request,'s_app/users.html',{'form':form})
