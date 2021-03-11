from django.conf.urls import url
from s_app import views


app_name = 's_app'

urlpatterns=[

      url(r'^$',views.users,name='users'),
      url(r'^users/$',views.users,name='users'),
      url(r'^index/$',views.index,name='index'),
]
