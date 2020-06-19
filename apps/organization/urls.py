# -*- coding:utf-8 -*-

from django.urls import path, re_path

from organization.views import OrgView, AddUserAskView

app_name = 'organization'

urlpatterns = [
	path('list/', OrgView.as_view(), name='org_list'),
	# 添加我要学习
	path('add_ask/', AddUserAskView.as_view(), name='add_ask')
]
