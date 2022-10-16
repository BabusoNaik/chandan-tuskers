"""s_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# from django.conf.urls import url
from django.urls import path
from s_app import views
from django.urls import include, re_path

from django.conf.urls import include

urlpatterns = [
    re_path(r'^$',views.IndexView.as_view(),name='index'),
    re_path(r'^s_app/',include('s_app.urls')),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$',views.AboutView.as_view(),name='about'),
    re_path(r'^$',views.SquadView.as_view(),name='squad'),
    re_path(r'^$',views.ThankView.as_view(),name='thanku'),

]
