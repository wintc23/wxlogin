from django.db import models

# Create your models here.


class WXUserInfo(models.Model):
    openid=models.CharField("openid")
    info_str=models.CharField("info_str")
    
