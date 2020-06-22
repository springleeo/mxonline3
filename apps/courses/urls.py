# -*- coding:utf-8 -*-
from django.urls import path

from courses.views import CourseListView

app_name = 'courses'

urlpatterns = [
	# 课程列表url
	path('list/', CourseListView.as_view(), name='list')
]
