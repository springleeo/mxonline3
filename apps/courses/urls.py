# -*- coding:utf-8 -*-
from django.urls import path, re_path

from courses.views import CourseListView, CourseDetailView, CourseInfoView

app_name = 'courses'

urlpatterns = [
    # 课程列表url
    path('list/', CourseListView.as_view(), name='list'),
    # 访问课程详情
    re_path('detail/(?P<course_id>\d+)/', CourseDetailView.as_view(), name="course_detail"),
    # 课程章节信息页
    re_path('info/(?P<course_id>\d+)/', CourseInfoView.as_view(), name='course_info'),
]
