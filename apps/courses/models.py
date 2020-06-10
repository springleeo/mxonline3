from datetime import datetime
from django.db import models


# 课程信息表
class Course(models.Model):
	DEGREE_CHOICES = (
		('cj', u'初级'),
		('zj', u'中级'),
		('gj', u'高级')
	)
	name = models.CharField('课程名', max_length=50)
	desc = models.CharField('课程描述', max_length=300)
	# TextField允许我们不输入长度。可以输入到无限大。暂时定义为TextFiled，之后更新为富文本
	detail = models.TextField('课程详情')
	degree = models.CharField('课程难度', choices=DEGREE_CHOICES, max_length=2)
	# 使用分钟做后台记录(存储最小单位)前台转换
	learn_times = models.IntegerField('学习时长(分钟数)', default=0)
	# 保存学习人数:点击开始学习才算
	students = models.IntegerField('学习人数', default=0)
	fav_nums = models.IntegerField('收藏人数', default=0)
	image = models.ImageField('封面图', upload_to='courses/%Y/%m', max_length=100)
	# 保存点击量，点进页面就算
	click_nums = models.IntegerField('点击数', default=0)
	add_time = models.DateTimeField('添加时间', default=datetime.now)

	class Meta:
		verbose_name = '课程'
		verbose_name_plural = verbose_name


# 章节
class Lesson(models.Model):
	# 因为一个课程对应很多章节。所以在章节表中将课程设置为外键。
	# 作为一个字段来让我们可以知道这个章节对应那个课程
	course = models.ForeignKey(Course, verbose_name='课程', on_delete=models.CASCADE)
	name = models.CharField('章节名', max_length=100)
	add_time = models.DateTimeField('添加时间', default=datetime.now)

	class Meta:
		verbose_name = '章节'
		verbose_name_plural = verbose_name


# 每章视频
class Video(models.Model):
	# 因为一个章节对应很多视频。所以在视频表中将章节设置为外键。
	# 作为一个字段来存储让我们可以知道这个视频对应哪个章节.
	lesson = models.ForeignKey(Lesson, verbose_name='章节', on_delete=models.CASCADE)
	name = models.CharField('视频名', max_length=100)
	add_time = models.DateTimeField('添加时间', default=datetime.now)

	class Meta:
		verbose_name = '视频'
		verbose_name_plural = verbose_name


# 课程资源
class CourseResource(models.Model):
	# 因为一个课程对应很多资源。所以在课程资源表中将课程设置为外键。
	# 作为一个字段来让我们可以知道这个资源对应那个课程
	course = models.ForeignKey(Course, verbose_name='课程', on_delete=models.CASCADE)
	name = models.CharField('名称', max_length=100)
	# 这里定义成文件类型的field，后台管理系统中会直接有上传的按钮。
	# FileField也是一个字符串类型，要指定最大长度。
	download = models.FileField('资源文件', upload_to='course/resource/%Y/%m', max_length=100)
	add_time = models.DateTimeField('添加时间', default=datetime.now)

	class Meta:
		verbose_name = '课程资源'
		verbose_name_plural = verbose_name
