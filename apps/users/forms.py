# -*- coding:utf-8 -*-
from django import forms
from captcha.fields import CaptchaField


# 登录表单验证
class LoginForm(forms.Form):
	# 用户名密码不能为空
	username = forms.CharField(required=True)
	# 密码不能小于5位
	password = forms.CharField(required=True, min_length=5)


class RegisterForm(forms.Form):
	# 此处email与前端name需保持一致。
	email = forms.EmailField(required=True)
	# 密码不能小于5位
	password = forms.CharField(required=True, min_length=5)
	# 应用验证码
	captcha = CaptchaField()
