from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser



class UserProfile(AbstractUser):
    """
    用户
    """
    name = models.CharField(max_length=30,null=True,blank=True,verbose_name="姓名")
    birthday = models.DateField(null=True,blank=True,verbose_name="出生年月")
    gender = models.CharField(max_length=6,choices=(("male",u"男"),("female","女")),default="保密")
    mobile = models.CharField(null=True,blank=True,max_length=11,verbose_name="电话")
    email = models.EmailField(max_length=100,null=True,blank=True,verbose_name="邮箱")
    # identifier = models.CharField(max_length=40, unique=True)
    # USERNAME_FIELD = 'identifier'

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = "用户"

    def __str__(self):
        return self.username

class VerifyCode(models.Model):
    """
    短信验证码
    """
    code = models.CharField(max_length=10,verbose_name="验证码")
    mobile = models.CharField(max_length=11,verbose_name="电话")

    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name = "短信验证码"
        verbose_name_plural = "短信验证码"

    def __str__(self):
        return self.code



