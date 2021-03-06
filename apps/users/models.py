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

    # 获取用户未读消息的数量
    def unread_nums(self):
        # 获取用户未读消息读数量
        from operation.models import UserMessage
        return UserMessage.objects.filter(user=self.id, has_read=0).count()


class EmailVerifyRecord(models.Model):
    SEND_CHOICES = (
        ('register', '注册'),
        ('forget', '找回密码'),
        ('update_email', '修改邮箱')
    )
    code = models.CharField('验证码', max_length=20)
    # 未设置null = true blank = true 默认不可为空
    email = models.EmailField('邮箱', max_length=50)
    send_type = models.CharField('发送验证码类型', choices=SEND_CHOICES, max_length=20)
    send_time = models.DateTimeField('发送时间', default=datetime.now)

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}({1})'.format(self.code, self.email)


class Banner(models.Model):
    title = models.CharField('标题', max_length=100)
    image = models.ImageField('轮播图', upload_to='banner/%Y/%m', max_length=100)
    url = models.URLField('访问地址', max_length=200)
    # 默认index很大靠后。想要靠前修改index值。
    index = models.IntegerField('顺序', default=100)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name

    # 重载__str__方法使后台不再直接显示object
    def __str__(self):
        return '{0}(位于第{1}位)'.format(self.title, self.index)
