from django.db import models

# Create your models here.


class WXUserInfo(models.Model):
    openid=models.TextField("openid")
    info_str=models.TextField("info_str")
    
