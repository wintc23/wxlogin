from django.shortcuts import render

from django.http import HttpResponseRedirect,HttpResponse
import json

import urllib
import json

# Create your views here.

APPID="wx2d1d6aa2f86768d7"
APP_SECRET="6c909d49659ee0598ba1d46638388d11"
REDIRECT_URI="https://wyr.me/login/weixin"

def generate_url_params(info):
    lst=[]
    for key,value in info:
        lst.append("%s=%s"%(key,value))
    info_str="&".join(lst)
    return info_str

def login(request):
    info=[
        ("appid",APPID),
        ("redirect_uri",REDIRECT_URI),
        ("response_type","code"),
        ("scope","snsapi_login"),
        ("state","xxx")] 
    url="https://open.weixin.qq.com/connect/qrconnect?%s#wechat_redirect"%generate_url_params(info)
    return HttpResponseRedirect(url)

def login_callback(request):
    code=request.GET.get('code')
    info=[
        ("appid",APPID),
        ("secret",APP_SECRET),
        ("code",code),
        ("grant_type","authorization_code"),
    ]
    url="https://api.weixin.qq.com/sns/oauth2/access_token?%s"%generate_url_params(info)
    
    response=urllib.request.urlopen(url)
    response_json=response.read()
    print(response_json)
    access_token=data.get("access_token")
    return HttpResponseRedirect(reverse("app:index"))
    
def index(request):
    return HttpResponse("<h1>login success</h1>")

def home(request):
    return HttpResponse("Hello~")


