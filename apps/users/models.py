from datetime import datetime

from django.db import models

from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    # 自定义的性别选择
    GENDER_CHOICES = (('male', '男'), ('female', '女'))
    # 昵称
    nick_name = models.CharField('昵称', max_length=50, default='')
    # 生日
    birthday = models.DateField('生日', null=True, blank=True)
    # 性别
    gender = models.CharField('性别', max_length=6, choices=GENDER_CHOICES, default='female')
    # 地址
    address = models.CharField('地址', max_length=100, default='')
    # 电话
    mobile = models.CharField('电话', max_length=11, null=True, blank=True)
    # 头像 默认使用default.png
    image = models.ImageField('头像', upload_to='image/%Y/%m', default='image/default.png', max_length=100)

    # 迁移报错： AttributeError: type object 'UserProfile' has no attribute 'USERNAME_FIELD'
    # 报错原因：继承了AbstractBaseUser，而不是AbstractUser
    # identifier = models.CharField(max_length=40, unique=True)
    # USERNAME_FIELD = 'identifier'

    # meta信息，即后台栏目名
    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    # 打印实例会打印username，username为继承自abstractuser
    def __str__(self):
        return self.username


