# -*- coding: utf-8 -*-

import sys
import os

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd + "../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mxonline3.settings")

import django

django.setup()
from organization.models import CityDict, CourseOrg, Teacher

city_dict_data = [
    {
        'name': '厦门',
        'desc': '厦门， 简称“厦”或“鹭”，别称鹭岛， 是福建省副省级市、计划单列市，国务院批复确定的中国经济特区，东南沿海重要的中心城市、港口及风景旅游城市',
    },
    {
        'name': '北京',
        'desc': '北京，简称“京”，古称燕京、北平，是中华人民共和国首都、省级行政区、直辖市、国家中心城市、超大城市，国务院批复确定的中国政治中心、文化中心、国际交往中心、科技创新中心。',
    },
    {
        'name': '上海',
        'desc': '上海，简称“沪”，是中华人民共和国省级行政区、直辖市、国家中心城市、超大城市，中国国际经济、金融、贸易、航运、科技创新中心，国家物流枢纽',
    },
    {
        'name': '福州',
        'desc': '福州，简称“榕”，别称榕城，是福建省省会，国务院批复确定的中国海峡西岸经济区中心城市之一、滨江滨海生态园林城市',
    },
    {
        'name': '杭州',
        'desc': '杭州，简称“杭”，古称临安、钱塘，是浙江省省会、副省级市、杭州都市圈核心城市，国务院批复确定的中国浙江省省会和全省经济、文化、科教中心、长江三角洲中心城市之一',
    },
    {
        'name': '广州',
        'desc': '广州，简称“穗”，别称羊城、花城，是广东省省会、副省级市、国家中心城市、超大城市，国务院批复确定的中国重要的中心城市、国际商贸中心和综合交通枢纽',
    },
    {
        'name': '南京',
        'desc': '南京，简称“宁”，古称金陵、建康，是江苏省会、副省级市、特大城市、南京都市圈核心城市，国务院批复确定的中国东部地区重要的中心城市、全国重要的科研教育基地和综合交通枢纽',
    },
    {
        'name': '成都',
        'desc': '成都，简称“蓉”，别称蓉城、锦城，是四川省省会、副省级市、特大城市、成都都市圈核心城市，国务院批复确定的中国西部地区重要的中心城市，国家重要的高新技术产业基地、商贸物流中心和综合交通枢纽',
    },
    {
        'name': '深圳',
        'desc': '深圳，简称“深”，别称鹏城，是广东省副省级市、计划单列市、超大城市，国务院批复确定的中国经济特区、全国性经济中心城市和国际化城市',
    },
    {
        'name': '天津',
        'desc': '天津，简称“津”，别称津沽、津门，是中华人民共和国省级行政区、直辖市、国家中心城市、超大城市，国务院批复确定的环渤海地区的经济中心',
    },
    {
        'name': '大连',
        'desc': '大连，别称滨城，是辽宁省副省级市、计划单列市，国务院批复确定的中国北方沿海重要的中心城市、港口及风景旅游城市',
    },
    {
        'name': '苏州',
        'desc': '苏州，简称“苏”，古称姑苏、平江，是江苏省地级市，国务院批复确定的中国长江三角洲重要的中心城市之一、国家高新技术产业基地和风景旅游城市',
    },
    {
        'name': '武汉',
        'desc': '武汉，简称“汉”，别称江城，是湖北省省会，中部六省唯一的副省级市，特大城市，国务院批复确定的中国中部地区的中心城市，全国重要的工业基地、科教基地和综合交通枢纽',
    },
]


def city_dict():
    for i in city_dict_data:
        check = CityDict.objects.filter(name=i['name'])
        if check:
            city = check
            city[0].name = i['name']
            city[0].desc = i['desc']
            city[0].save()
        else:
            city = CityDict()
            city.name = i['name']
            city.desc = i['desc']
            city.save()


course_org_data = [
    {
        'name': '新东方',
        'desc': '新东方，全名北京新东方教育科技（集团）有限公司，总部位于中国北京市海淀区中关村，是综合性教育集团，同时也是教育培训集团。',
        'category': 'pxjg',
        'click_nums': '12',
        'fav_nums': '115',
        'image': 'org/2020/06/xindongfang.jpg',
        'address': '中国北京海淀区',
        'city': '北京',
    },
    {
        'name': '优学教育',
        'desc': '优学环球教育集团是中国最大的教育连锁机构之一',
        'category': 'pxjg',
        'click_nums': '15',
        'fav_nums': '105',
        'image': 'org/2020/06/youxuejiaoyu.jpg',
        'address': '中国上海',
        'city': '上海',
    },
    {
        'name': '卓越教育',
        'desc': '卓越教育是全国领先的，华南较大的中小学课外教育机构',
        'category': 'pxjg',
        'click_nums': '1011',
        'fav_nums': '1035',
        'image': 'org/2020/06/zhuoyuejiaoyu.jpg',
        'address': '广东深圳',
        'city': '深圳',
    },
    {
        'name': '北京师范大学',
        'desc': '北京师范大学是中华人民共和国教育部直属、中央直管副部级建制的全国重点大学，位列“双一流”、“985工程”、“211工程”，国家“七五”、“八五”首批重点建设十所大学之一',
        'category': 'gx',
        'click_nums': '15',
        'fav_nums': '105',
        'image': 'org/2020/06/beijingshifan.jpg',
        'address': '中国北京',
        'city': '北京',
    },
    {
        'name': '福建师范大学',
        'desc': '福建师范大学是福建省人民政府与中华人民共和国教育部共建高校，福建省“双一流”建设高校，省属重点综合性大学',
        'category': 'gx',
        'click_nums': '151',
        'fav_nums': '1015',
        'image': 'org/2020/06/fujianshifan.jpg',
        'address': '福建',
        'city': '福州',
    },
    {
        'name': '厦门大学',
        'desc': '厦门大学是由中华人民共和国教育部直属、中央直管副部级建制的综合性研究型全国重点大学',
        'category': 'gx',
        'click_nums': '312',
        'fav_nums': '100003',
        'image': 'org/2020/06/xiamendaxue.jpg',
        'address': '福建厦门',
        'city': '厦门',
    },
    {
        'name': '桔子摄影',
        'desc': '欧美风',
        'category': 'gr',
        'click_nums': '82',
        'fav_nums': '302',
        'image': 'org/2020/06/juzisheying.jpg',
        'address': '成都',
        'city': '成都',
    },
    {
        'name': '后古婚纱',
        'desc': '婚纱',
        'category': 'gr',
        'click_nums': '1',
        'fav_nums': '24',
        'image': 'org/2020/06/houguhunsha.jpg',
        'address': '福建厦门',
        'city': '厦门',
    },
    {
        'name': '大城小爱',
        'desc': '日系风格',
        'category': 'gr',
        'click_nums': '21',
        'fav_nums': '34',
        'image': 'org/2020/06/dachengxiaoai.jpg',
        'address': '深圳',
        'city': '深圳',
    },
]


def course_org():
    for i in course_org_data:
        check = CourseOrg.objects.filter(name=i['name'])
        if check:
            course = check
            course[0].name = i['name']
            course[0].desc = i['desc']
            course[0].category = i['category']
            course[0].click_nums = i['click_nums']
            course[0].fav_nums = i['fav_nums']
            course[0].image = i['image']
            course[0].address = i['address']
            course[0].city_id = CityDict.objects.get(name=i['city']).id
            course[0].save()
        else:
            course = CourseOrg()
            course.name = i['name']
            course.desc = i['desc']
            course.category = i['category']
            course.click_nums = i['click_nums']
            course.fav_nums = i['fav_nums']
            course.image = i['image']
            course.address = i['address']
            course.city_id = CityDict.objects.get(name=i['city']).id
            course.save()


teacher_data = [
    {
        'org': '新东方',
        'name': '愈敏洪',
        'work_years': '5',
        'work_company': '新东方',
        'work_position': '总裁',
        'points': '幽默',
        'click_nums': '3',
        'fav_nums': '1',
    },
	{
		'org': '新东方',
		'name': '周杰伦',
		'work_years': '1',
		'work_company': '新东方',
		'work_position': '英语老师',
		'points': '唱歌好听',
		'click_nums': '3',
		'fav_nums': '10',
	},
	{
		'org': '优学教育',
		'name': '林俊杰',
		'work_years': '9',
		'work_company': '优学教育',
		'work_position': '钢琴老师',
		'points': '指法芬芳',
		'click_nums': '5',
		'fav_nums': '123',
	},
	{
		'org': '厦门大学',
		'name': '刘德华',
		'work_years': '1',
		'work_company': '厦门大学',
		'work_position': '唱跳老师',
		'points': '唱跳',
		'click_nums': '5',
		'fav_nums': '1232',
	},
	{
		'org': '福建师范大学',
		'name': '李荣浩',
		'work_years': '11',
		'work_company': '福建师范大学',
		'work_position': '创作老师',
		'points': '创作',
		'click_nums': '0',
		'fav_nums': '18',
	},
	{
		'org': '桔子摄影',
		'name': '邓紫棋',
		'work_years': '4',
		'work_company': '桔子摄影',
		'work_position': '修图老师',
		'points': '修图',
		'click_nums': '0',
		'fav_nums': '180',
	},
	{
		'org': '后古婚纱',
		'name': '毛不易',
		'work_years': '3',
		'work_company': '后古婚纱',
		'work_position': '摄影师',
		'points': '拍照',
		'click_nums': '0',
		'fav_nums': '180',
	},
	{
		'org': '大城小爱',
		'name': '汪苏泷',
		'work_years': '10',
		'work_company': '大城小爱',
		'work_position': '灯光师',
		'points': '灯光',
		'click_nums': '0',
		'fav_nums': '180',
	},

]


def teacher():
    for i in teacher_data:
        check = Teacher.objects.filter(name=i['name'])
        if check:
            teacher = check
            teacher[0].name = i['name']
            teacher[0].work_years = i['work_years']
            teacher[0].work_company = i['work_company']
            teacher[0].work_position = i['work_position']
            teacher[0].points = i['points']
            teacher[0].click_nums = i['click_nums']
            teacher[0].fav_nums = i['fav_nums']
            teacher[0].org_id = CourseOrg.objects.get(name=i['org']).id
            teacher[0].save()
        else:
            teacher = Teacher()
            teacher.name = i['name']
            teacher.work_years = i['work_years']
            teacher.work_company = i['work_company']
            teacher.work_position = i['work_position']
            teacher.points = i['points']
            teacher.click_nums = i['click_nums']
            teacher.fav_nums = i['fav_nums']
            teacher.org_id = CourseOrg.objects.get(name=i['org']).id
            teacher.save()


if __name__ == '__main__':
    # city_dict()
    course_org()
    teacher()