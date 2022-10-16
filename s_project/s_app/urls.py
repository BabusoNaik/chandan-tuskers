# from django.conf.urls import url
from django.urls import include, re_path
from s_app import views
from . import views


app_name = 's_app'

urlpatterns=[

      re_path(r'^$',views.users,name='users'),
      re_path(r'^users/$',views.users,name='users'),
      re_path(r'^index/$',views.IndexView.as_view(),name='index'),
      re_path(r'^about/$',views.AboutView.as_view(),name='about'),
      re_path(r'^squad/$',views.SquadView.as_view(),name='squad'),
      re_path(r'^thanku/$',views.ThankView.as_view(),name='thanku'),


]
