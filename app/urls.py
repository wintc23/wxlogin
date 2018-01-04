from django.urls import path

from . import views

app_name="app"

urlpatterns=[
     path("login",views.login,name="login"),
     path("login/weixin/",views.login_callback,name="login_callback"),
     path("index/",views.index,name="index"),
     path("",views.home,name="home"),
 ]
