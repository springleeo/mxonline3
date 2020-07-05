# -*- coding:utf-8 -*-
from django.urls import path, re_path

from users.views import UserinfoView

app_name = 'users'

urlpatterns = [
	# 课程列表url
	path('info/', UserinfoView.as_view(), name='user_info'),

]
