# -*- coding:utf-8 -*-
from django.urls import path, re_path

from courses.views import CourseListView, CourseDetailView

app_name = 'courses'

urlpatterns = [
    # 课程列表url
    path('list/', CourseListView.as_view(), name='list'),
    # 访问课程详情
    re_path('detail/(?P<course_id>\d+)/', CourseDetailView.as_view(), name="course_detail"),
]
