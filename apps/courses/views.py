from django.http import HttpResponse
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.views import View

from courses.models import Course, CourseResource
from operation.models import UserFavorite, CourseComments


class CourseListView(View):
	def get(self, request):
		all_course = Course.objects.all()
		# 热门课程推荐
		hot_courses = Course.objects.all().order_by("-students")[:3]
		# 对课程进行分页
		# 尝试获取前台get请求传递过来的page参数
		# 如果是不合法的配置参数默认返回第一页
		# 进行排序
		sort = request.GET.get('sort', "")
		if sort:
			if sort == "students":
				all_course = all_course.order_by("-students")
			elif sort == "hot":
				all_course = all_course.order_by("-click_nums")
		try:
			page = request.GET.get('page', 1)
		except PageNotAnInteger:
			page = 1
		# 这里指从allorg中取五个出来，每页显示5个
		p = Paginator(all_course, 6, request=request)
		courses = p.page(page)
		return render(request, "course-list.html", {
			"all_course": courses,
			"sort": sort,
			"hot_courses": hot_courses,
		})


class CourseDetailView(View):
	def get(self, request, course_id):
		course = Course.objects.get(id=int(course_id))

		# 增加课程点击数
		course.click_nums += 1
		course.save()

		# 是否收藏课程
		has_fav_course = False
		has_fav_org = False

		# 必须是用户已登录我们才需要判断。
		if request.user.is_authenticated:
			if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=1):
				has_fav_course = True
			if UserFavorite.objects.filter(user=request.user, fav_id=course.course_org.id, fav_type=2):
				has_fav_org = True

		# 取出标签找到标签相同的course
		tag = course.tag
		if tag:
			# 从1开始否则会推荐自己
			relate_courses = Course.objects.filter(tag=tag)[1:2]
		else:
			relate_courses = []

		return render(request, "course-detail.html", {
			"course": course,
			"relate_courses": relate_courses,
			"has_fav_course": has_fav_course,
			"has_fav_org": has_fav_org,
		})


class CourseInfoView(View):
	'''课程章节信息'''

	def get(self, request, course_id):
		course = Course.objects.get(id=int(course_id))
		all_resources = CourseResource.objects.filter(course=course)

		return render(request, "course-video.html", {
			"course": course,
			"all_resources": all_resources,
		})


class CommentsView(View):
	def get(self, request, course_id):
		# 此处的id为表默认为我们添加的值。
		course = Course.objects.get(id=int(course_id))
		all_resources = CourseResource.objects.filter(course=course)
		all_comments = CourseComments.objects.all()
		return render(request, "course-comment.html", {
			"course": course,
			"all_resources": all_resources,
			"all_comments": all_comments,
		})


# ajax方式添加评论
class AddCommentsView(View):
	def post(self, request):
		if not request.user.is_authenticated:
			# 未登录时返回json提示未登录，跳转到登录页面是在ajax中做的
			return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')
		course_id = request.POST.get("course_id", 0)
		comments = request.POST.get("comments", "")
		if int(course_id) > 0 and comments:
			course_comments = CourseComments()
			# get只能取出一条数据，如果有多条抛出异常。没有数据也抛异常
			# filter取一个列表出来，queryset。没有数据返回空的queryset不会抛异常
			course = Course.objects.get(id=int(course_id))
			# 外键存入要存入对象
			course_comments.course = course
			course_comments.comments = comments
			course_comments.user = request.user
			course_comments.save()
			return HttpResponse('{"status":"success", "msg":"评论成功"}', content_type='application/json')
		else:
			return HttpResponse('{"status":"fail", "msg":"评论失败"}', content_type='application/json')
