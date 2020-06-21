# -*- coding:utf-8 -*-

from django.urls import path, re_path

from organization.views import OrgView, AddUserAskView, OrgHomeView

app_name = 'organization'

urlpatterns = [
    path('list/', OrgView.as_view(), name='org_list'),
    # 添加我要学习
    path('add_ask/', AddUserAskView.as_view(), name='add_ask'),
    # 机构home页面
    re_path('home/(?P<org_id>\d+)/', OrgHomeView.as_view(), name="org_home"),
]
