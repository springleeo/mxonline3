# -*- coding:utf-8 -*-
from django.urls import path, re_path

from users.views import UserinfoView, UploadImageView, UpdatePwdView, SendEmailCodeView, UpdateEmailView

app_name = 'users'

urlpatterns = [
    # 课程列表url
    path('info/', UserinfoView.as_view(), name='user_info'),
    # 用户头像上传
    path('image/upload/', UploadImageView.as_view(), name='image_upload'),
    # 修改用户密码
    path('update/pwd/', UpdatePwdView.as_view(), name='update_pwd'),
    # 发送邮箱验证码
    path('sendemail_code/', SendEmailCodeView.as_view(), name='sendemail_code'),
    # 修改邮箱
    path('update_email/', UpdateEmailView.as_view(), name='update_email'),

]
