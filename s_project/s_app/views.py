from django.shortcuts import render
from django.http import HttpResponse
# from s_app.models import User
from s_app.forms import NewUser
from django.views.generic import View, TemplateView
from . import forms

# Create your views here.
class ThankView(TemplateView):
    template_name = 's_app/thanku.html'
    
def thanku(request):
    return render(request,'s_app/thanku.html')


class SquadView(TemplateView):
    template_name = 's_app/squad.html'
# def squad(request):

#     return render(request,'s_app/squad.html')

class AboutView(TemplateView):
    template_name = 's_app/about.html'
# def about(request):

#     return render(request,'s_app/about.html')


class IndexView(TemplateView):
    template_name = 's_app/index.html'
    
class GallaryView(TemplateView):
    template_name = 's_app/gallary.html'
# def index(request):

#     return render(request,'s_app/index.html')


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
