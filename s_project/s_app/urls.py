from django.conf.urls import url
from s_app import views

urlpatterns=[
      
      url(r'^$',views.users,name='users'),
]
