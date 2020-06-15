from django.shortcuts import render
from django.views.generic.base import View

# 处理课程结构列表大view
from organization.models import CourseOrg, CityDict


class OrgView(View):
    def get(self, request):
        # 查找到所有的课程机构
        all_orgs = CourseOrg.objects.all()
        #  取出所有城市
        all_citys = CityDict.objects.all()

        return render(request, 'org-list.html', {"all_orgs": all_orgs,
                                                 "all_citys": all_citys, })
