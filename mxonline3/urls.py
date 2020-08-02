"""mxonline3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve


import xadmin
from django.views.generic import TemplateView

from mxonline3.settings import MEDIA_ROOT, STATIC_ROOT
from organization.views import OrgView
from users.views import IndexView
from users.views import LoginView, RegisterView, ActiveUserView, ForgetPwdView, ResetView, ModifyPwdView, LogoutView
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('', IndexView.as_view(), name='index'),
    # path('login/', TemplateView.as_view(template_name='login.html'), name='login')
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    # 验证码url
    path("captcha/", include('captcha.urls')),
    # 激活用户url
    re_path('active/(?P<active_code>.*)/', ActiveUserView.as_view(), name='user_active'),
    # 忘记密码
    path('forget/', ForgetPwdView.as_view(), name='forget_pwd'),
    # 重置密码，用来接收来自邮箱的重置链接
    re_path('reset/(?P<active_code>.*)/', ResetView.as_view(), name='reset_pwd'),
    # 修改密码，用于passwordreset页面提交表单
    path('modify_pwd/', ModifyPwdView.as_view(), name='modify_pwd'),
    # 课程机构首页url
    # path('org_list/', OrgView.as_view(), name='org_list'),
    path('org/', include('organization.urls', namespace='org')),
    # 课程app的url配置
    path('course/', include('courses.urls', namespace='course')),
    # 个人信息
    path('users/', include('users.urls', namespace='users')),
    # 处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找，我们有配置好的路径MEDIAROOT
    re_path(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)', serve, {"document_root": STATIC_ROOT}, name='static'),

]
# 全局404页面配置
handler404 = 'users.views.pag_not_found'
# 全局500页面配置
handler500 = 'users.views.page_error'
