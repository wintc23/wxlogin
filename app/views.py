from django.shortcuts import render
from django.urls import reverse
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
    data=get_jsondata_by_url(url)
    access_token=data.get('access_token')
    openid=data.get('openid')
    user_data=get_user_info(access_token,openid)
    return HttpResponse("%s"%user_data)

def get_jsondata_by_url(url):
    response=urllib.request.urlopen(url)
    response_json=response.read().decode("utf-8")
    print(response_json)
    data=json.loads(response_json)
    return data

def get_user_info(access_token,openid):
    info=[('access_token',access_token),('openid',openid)]
    url="https://api.weixin.qq.com/sns/userinfo?%s"%generate_url_params(info)
    data=get_jsondata_by_url(url)
    return data


def index(request):
    return HttpResponse("<h1>login success</h1>")

def home(request):
    return HttpResponse("Hello~")


