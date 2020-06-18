from django.shortcuts import render
from django.views.generic.base import View

# 处理课程结构列表大view
from organization.models import CourseOrg, CityDict
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger


class OrgView(View):
	def get(self, request):
		# 查找到所有的课程机构
		all_orgs = CourseOrg.objects.all()

		org_nums = all_orgs.count()
		#  取出所有城市
		all_citys = CityDict.objects.all()

		# 取出筛选的城市,默认值为空
		city_id = request.GET.get('city', "")
		# 如果选择了某个城市,也就是前端传过来了值
		if city_id:
			# 外键city在数据中叫city_id
			# 我们就在机构中作进一步筛选
			all_orgs = all_orgs.filter(city_id=int(city_id))

		# 类别筛选
		category = request.GET.get('ct', "")
		if category:
			# 我们就在机构中作进一步筛选类别
			all_orgs = all_orgs.filter(category=category)

		# 对课程机构进行分页
		# 尝试获取前台get请求传递过来的page参数
		# 如果是不合法的配置参数默认返回第一页
		try:
			page = request.GET.get('page', 1)
		except PageNotAnInteger:
			page = 1

		# 这里指从allorg中取2个出来，每页显示2个
		p = Paginator(all_orgs, 2, request=request)
		orgs = p.page(page)

		return render(request, 'org-list.html', {"all_orgs": orgs,
		                                         "all_citys": all_citys,
		                                         'org_nums': org_nums,
		                                         'city_id': city_id,
		                                         "category": category, })
