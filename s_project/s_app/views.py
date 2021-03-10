from django.shortcuts import render
from django.http import HttpResponse
# from s_app.models import User
from s_app.forms import NewUser
from . import forms

# Create your views here.

def index(request):
    my_dict = {'insert_me':'Hello...s_app'}
    return render(request,'s_app/index.html',context=my_dict)


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

def form_name_view(request):
    form = forms.FormName()

    if request.method=='POST':
         form = forms.FormName(request.POST)

         if form.is_valid():

              print("success")
              print("NAME:" +form.cleaned_data['name'])
              print("EMAIL:" +form.cleaned_data['email'])
              print("TEXT:" +form.cleaned_data['text'])




    return render(request,'s_app/form.html',{'form':form})
