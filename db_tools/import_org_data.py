# -*- coding: utf-8 -*-

import sys
import os

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd + "../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mxonline3.settings")

import django
from django.db.models import Q

django.setup()
from organization.models import CityDict, CourseOrg, Teacher
from courses.models import Course, Lesson

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
        'course_nums': '26',
        'students': '2003',
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
        'course_nums': '260',
        'students': '213',
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
        'course_nums': '526',
        'students': '12003',
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
        'course_nums': '256',
        'students': '200',
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
        'course_nums': '278',
        'students': '201',
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
        'course_nums': '34',
        'students': '27',
    },
    {
        'name': '清华大学',
        'desc': '清华大学（Tsinghua University），简称“清华”，是中华人民共和国教育部直属、中央直管副部级建制的全国重点大学',
        'category': 'gx',
        'click_nums': '312',
        'fav_nums': '100003',
        'image': 'org/2020/06/qinghuadaxue.jpg',
        'address': '北京',
        'city': '北京',
        'course_nums': '34',
        'students': '27',
    },
    {
        'name': '武汉大学',
        'desc': '武汉大学与中国光大集团开启战略合作 将在高端人才培养与智库建设、科学研究、金融与实业等领域开展合作',
        'category': 'gx',
        'click_nums': '6',
        'fav_nums': '8',
        'image': 'org/2020/06/wuhandaxue.jpg',
        'address': '武汉',
        'city': '武汉',
        'course_nums': '34',
        'students': '27',
    },
    {
        'name': '北京大学',
        'desc': '北京大学（Peking University），简称“北大”，由中华人民共和国教育部直属，中央直管副部级建制，位列“世界一流大学和一流学科”',
        'category': 'gx',
        'click_nums': '32',
        'fav_nums': '64',
        'image': 'org/2020/06/beijingdaxue.jpg',
        'address': '北京',
        'city': '北京',
        'course_nums': '34',
        'students': '27',
    },
    {
        'name': '南京大学',
        'desc': '南京大学（Nanjing University），简称“南大”，是中华人民共和国教育部直属的全国重点大学，位列世界一流大学建设高校”',
        'category': 'gx',
        'click_nums': '39',
        'fav_nums': '63',
        'image': 'org/2020/06/nanjingdaxue.jpg',
        'address': '南京',
        'city': '南京',
        'course_nums': '11',
        'students': '2',
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
        'course_nums': '89',
        'students': '87',
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
        'course_nums': '250',
        'students': '61',
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
        'course_nums': '2',
        'students': '65',
    },
]


def course_org():
    key_name = []
    for key in CourseOrg._meta.get_fields():
        try:
            if key.attname not in ['id', 'add_time']:
                key_name.append(key.attname)
        except:
            pass
    for i in course_org_data:
        check = CourseOrg.objects.filter(name=i['name'])
        if check:
            course = check
            for j in key_name:
                if j == 'city_id':
                    course[0].city_id = CityDict.objects.get(name=i['city']).id
                else:
                    course[0].__setattr__(j, i[j])
            course[0].save()
        else:
            course = CourseOrg()
            for j in key_name:
                if j == 'city_id':
                    course.city_id = CityDict.objects.get(name=i['city']).id
                else:
                    course.__setattr__(j, i[j])
            course.save()


teacher_data = [
    {
        'org': '新东方',
        'name': '愈敏洪',
        'image': 'teacher/2020/06/yuminhong.jpg',
        'work_years': '1436',
        'work_company': '新东方',
        'work_position': '总裁',
        'points': '幽默',
        'click_nums': '3',
        'fav_nums': '1',
    },
    {
        'org': '新东方',
        'name': '周杰伦',
        'image': 'teacher/2020/06/zhoujielun.jpg',
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
        'image': 'teacher/2020/06/linjunjie.jpg',
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
        'image': 'teacher/2020/06/liudehua.jpg',
        'work_years': '1',
        'work_company': '厦门大学',
        'work_position': '唱跳老师',
        'points': '唱跳',
        'click_nums': '5',
        'fav_nums': '1232',
    },
    {
        'org': '北京大学',
        'name': '蔡徐坤',
        'image': 'teacher/2020/06/caixukun.jpg',

        'work_years': '11',
        'work_company': '北京大学',
        'work_position': '唱跳老师',
        'points': '唱跳',
        'click_nums': '59',
        'fav_nums': '67',
    },
    {
        'org': '北京大学',
        'name': '腾格尔',
        'image': 'teacher/2020/06/tenggeer.jpg',
        'work_years': '11',
        'work_company': '北京大学',
        'work_position': '美声老师',
        'points': '美声',
        'click_nums': '9',
        'fav_nums': '7',
    },
    {
        'org': '北京大学',
        'name': '张杰',
        'image': 'teacher/2020/06/zhangjie.jpg',
        'work_years': '1',
        'work_company': '北京大学',
        'work_position': '美声老师',
        'points': '美声',
        'click_nums': '9',
        'fav_nums': '2',
    },
    {
        'org': '南京大学',
        'name': '刘若英',
        'image': 'teacher/2020/06/liuruoying.jpg',
        'work_years': '17',
        'work_company': '南京大学',
        'work_position': '美声老师',
        'points': '美声',
        'click_nums': '19',
        'fav_nums': '67',
    },
    {
        'org': '武汉大学',
        'name': '薛之谦',
        'image': 'teacher/2020/06/xuezhiqian.jpg',
        'work_years': '17',
        'work_company': '武汉大学',
        'work_position': '美声老师',
        'points': '美声',
        'click_nums': '2',
        'fav_nums': '1',
    },
    {
        'org': '清华大学',
        'name': '韩红',
        'image': 'teacher/2020/06/hanhong.jpg',
        'work_years': '27',
        'work_company': '清华大学',
        'work_position': '美声老师',
        'points': '美声',
        'click_nums': '14',
        'fav_nums': '167',
    },
    {
        'org': '福建师范大学',
        'name': '李荣浩',
        'image': 'teacher/2020/06/lironghao.jpg',
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
        'image': 'teacher/2020/06/dengziqi.jpg',
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
        'image': 'teacher/2020/06/maobuyi.jpg',
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
        'image': 'teacher/2020/06/wangsulong.jpg',
        'work_years': '10',
        'work_company': '大城小爱',
        'work_position': '灯光师',
        'points': '灯光',
        'click_nums': '0',
        'fav_nums': '180',
    },

]


def teacher():
    key_name = []
    for key in Teacher._meta.get_fields():
        if key.attname not in ['id', 'add_time']:
            key_name.append(key.attname)

    for i in teacher_data:
        check = Teacher.objects.filter(name=i['name'])
        if check:
            teacher = check
            for j in key_name:
                if j == 'org_id':
                    teacher[0].org_id = CourseOrg.objects.get(name=i['org']).id
                else:
                    teacher[0].__setattr__(j, i[j])
            teacher[0].save()
        else:
            teacher = Teacher()
            for j in key_name:
                if j == 'org_id':
                    teacher.org_id = CourseOrg.objects.get(name=i['org']).id
                else:
                    teacher.__setattr__(j, i[j])
            teacher.save()


course_data = [
    {
        'name': '语文',
        'desc': '语文',
        'detail': '语文，是语言文字、语言文学、语言文化的简称。语言包括口头语言和书面语言。口头语言较随意，直接易懂，而书面语言讲究准确和语法；文学包括中外古今文学等',
        'degree': 'cj',
        'learn_times': '12',
        'students': '100',
        'fav_nums': '23',
        'image': 'courses/2020/06/yuwen.jpg',
        'click_nums': '12',
        'course_org': '新东方',
        'tag': '1',
        'category': '公共课',
        'teacher': '愈敏洪',
    },
    {
        'name': '语文',
        'desc': '语文',
        'detail': '语文，是语言文字、语言文学、语言文化的简称。语言包括口头语言和书面语言。口头语言较随意，直接易懂，而书面语言讲究准确和语法；文学包括中外古今文学等',
        'degree': 'cj',
        'learn_times': '12',
        'students': '10',
        'fav_nums': '2',
        'image': 'courses/2020/06/yuwen.jpg',
        'click_nums': '12',
        'course_org': '厦门大学',
        'tag': '1',
        'category': '公共课',
        'teacher': '刘德华',
    },
    {
        'name': '语文',
        'desc': '语文',
        'detail': '语文，是语言文字、语言文学、语言文化的简称。语言包括口头语言和书面语言。口头语言较随意，直接易懂，而书面语言讲究准确和语法；文学包括中外古今文学等',
        'degree': 'cj',
        'learn_times': '56',
        'students': '49',
        'fav_nums': '34',
        'image': 'courses/2020/06/yuwen.jpg',
        'click_nums': '62',
        'course_org': '北京师范大学',
        'tag': '1',
        'category': '公共课',
        'teacher': '',
    },
    {
        'name': '语文',
        'desc': '语文',
        'detail': '语文，是语言文字、语言文学、语言文化的简称。语言包括口头语言和书面语言。口头语言较随意，直接易懂，而书面语言讲究准确和语法；文学包括中外古今文学等',
        'degree': 'gj',
        'learn_times': '40',
        'students': '12',
        'fav_nums': '69',
        'image': 'courses/2020/06/yuwen.jpg',
        'click_nums': '63',
        'course_org': '清华大学',
        'tag': '1',
        'category': '公共课',
        'teacher': '',
    },
    {
        'name': '语文',
        'desc': '语文',
        'detail': '语文，是语言文字、语言文学、语言文化的简称。语言包括口头语言和书面语言。口头语言较随意，直接易懂，而书面语言讲究准确和语法；文学包括中外古今文学等',
        'degree': 'gj',
        'learn_times': '43',
        'students': '13',
        'fav_nums': '60',
        'image': 'courses/2020/06/yuwen.jpg',
        'click_nums': '93',
        'course_org': '北京大学',
        'tag': '1',
        'category': '公共课',
        'teacher': '',
    },
    {
        'name': '数学',
        'desc': '数学',
        'detail': '数学（mathematics或maths，其英文来自希腊语，“máthēma”；经常被缩写为“math”），是研究数量、结构、变化、空间以及信息等概念的一门学科，从某种角度看属于形式科学的一种。数学家和哲学家对数学的确切范围和定义有一系列的看法',
        'degree': 'gj',
        'learn_times': '7',
        'students': '45',
        'fav_nums': '90',
        'image': 'courses/2020/06/shuxue.jpg',
        'click_nums': '8000',
        'course_org': '新东方',
        'tag': '2',
        'category': '公共课',
        'teacher': '周杰伦',
    },
    {
        'name': '数学',
        'desc': '数学',
        'detail': '数学（mathematics或maths，其英文来自希腊语，“máthēma”；经常被缩写为“math”），是研究数量、结构、变化、空间以及信息等概念的一门学科，从某种角度看属于形式科学的一种。数学家和哲学家对数学的确切范围和定义有一系列的看法',
        'degree': 'gj',
        'learn_times': '430',
        'students': '313',
        'fav_nums': '360',
        'image': 'courses/2020/06/shuxue.jpg',
        'click_nums': '93',
        'course_org': '北京大学',
        'tag': '2',
        'category': '公共课',
        'teacher': '',
    },
    {
        'name': '数学',
        'desc': '数学',
        'detail': '数学（mathematics或maths，其英文来自希腊语，“máthēma”；经常被缩写为“math”），是研究数量、结构、变化、空间以及信息等概念的一门学科，从某种角度看属于形式科学的一种。数学家和哲学家对数学的确切范围和定义有一系列的看法',
        'degree': 'gj',
        'learn_times': '390',
        'students': '43',
        'fav_nums': '560',
        'image': 'courses/2020/06/shuxue.jpg',
        'click_nums': '930',
        'course_org': '清华大学',
        'tag': '2',
        'category': '公共课',
        'teacher': '',
    },
    {
        'name': '数学',
        'desc': '数学',
        'detail': '数学（mathematics或maths，其英文来自希腊语，“máthēma”；经常被缩写为“math”），是研究数量、结构、变化、空间以及信息等概念的一门学科，从某种角度看属于形式科学的一种。数学家和哲学家对数学的确切范围和定义有一系列的看法',
        'degree': 'gj',
        'learn_times': '874',
        'students': '471',
        'fav_nums': '508',
        'image': 'courses/2020/06/shuxue.jpg',
        'click_nums': '190',
        'course_org': '武汉大学',
        'tag': '2',
        'category': '公共课',
        'teacher': '',
    },
    {
        'name': '英语',
        'desc': '英语',
        'detail': '英语是一种西日耳曼语，在中世纪早期的英国最早被使用，并因其广阔的殖民地而成为世界使用面积最广的语言',
        'degree': 'zj',
        'learn_times': '71',
        'students': '42',
        'fav_nums': '40',
        'image': 'courses/2020/06/yingyu.jpg',
        'click_nums': '80',
        'course_org': '新东方',
        'tag': '3',
        'category': '公共课',
        'teacher': '',
    },
    {
        'name': '英语',
        'desc': '英语',
        'detail': '英语是一种西日耳曼语，在中世纪早期的英国最早被使用，并因其广阔的殖民地而成为世界使用面积最广的语言',
        'degree': 'zj',
        'learn_times': '79',
        'students': '41',
        'fav_nums': '404',
        'image': 'courses/2020/06/yingyu.jpg',
        'click_nums': '80',
        'course_org': '南京大学',
        'tag': '3',
        'category': '公共课',
        'teacher': '',
    },
    {
        'name': '英语',
        'desc': '英语',
        'detail': '英语是一种西日耳曼语，在中世纪早期的英国最早被使用，并因其广阔的殖民地而成为世界使用面积最广的语言',
        'degree': 'zj',
        'learn_times': '79',
        'students': '41',
        'fav_nums': '404',
        'image': 'courses/2020/06/yingyu.jpg',
        'click_nums': '80',
        'course_org': '武汉大学',
        'tag': '3',
        'category': '公共课',
        'teacher': '',
    },
    {
        'name': '英语',
        'desc': '英语',
        'detail': '英语是一种西日耳曼语，在中世纪早期的英国最早被使用，并因其广阔的殖民地而成为世界使用面积最广的语言',
        'degree': 'zj',
        'learn_times': '719',
        'students': '487',
        'fav_nums': '4014',
        'image': 'courses/2020/06/yingyu.jpg',
        'click_nums': '800',
        'course_org': '厦门大学',
        'tag': '3',
        'category': '公共课',
        'teacher': '',
    },
    {
        'name': '英语',
        'desc': '英语',
        'detail': '英语是一种西日耳曼语，在中世纪早期的英国最早被使用，并因其广阔的殖民地而成为世界使用面积最广的语言',
        'degree': 'cj',
        'learn_times': '102',
        'students': '14',
        'fav_nums': '11',
        'image': 'courses/2020/06/yingyu.jpg',
        'click_nums': '10',
        'course_org': '福建师范大学',
        'tag': '3',
        'category': '公共课',
        'teacher': '',
    },
    {
        'name': 'python',
        'desc': 'python',
        'detail': 'Python是一种跨平台的计算机程序设计语言。',
        'degree': 'cj',
        'learn_times': '192',
        'students': '15',
        'fav_nums': '1012',
        'image': 'courses/2020/06/python.jpg',
        'click_nums': '10',
        'course_org': '福建师范大学',
        'tag': '4',
        'category': '专业课',
        'teacher': '',
    },
    {
        'name': 'python',
        'desc': 'python',
        'detail': 'Python是一种跨平台的计算机程序设计语言。',
        'degree': 'gj',
        'learn_times': '192',
        'students': '15',
        'fav_nums': '1012',
        'image': 'courses/2020/06/python.jpg',
        'click_nums': '10',
        'course_org': '清华大学',
        'tag': '4',
        'category': '专业课',
        'teacher': '',
    },
    {
        'name': 'python',
        'desc': 'python',
        'detail': 'Python是一种跨平台的计算机程序设计语言。',
        'degree': 'zj',
        'learn_times': '1634',
        'students': '15',
        'fav_nums': '1012',
        'image': 'courses/2020/06/python.jpg',
        'click_nums': '3',
        'course_org': '卓越教育',
        'tag': '4',
        'category': '专业课',
        'teacher': '',
    },
    {
        'name': 'python',
        'desc': 'python',
        'detail': 'Python是一种跨平台的计算机程序设计语言。',
        'degree': 'gj',
        'learn_times': '174',
        'students': '19',
        'fav_nums': '196',
        'image': 'courses/2020/06/python.jpg',
        'click_nums': '31',
        'course_org': '优学教育',
        'tag': '4',
        'category': '专业课',
        'teacher': '',
    },
    {
        'name': 'python',
        'desc': 'python',
        'detail': 'Python是一种跨平台的计算机程序设计语言。',
        'degree': 'cj',
        'learn_times': '4',
        'students': '191',
        'fav_nums': '136',
        'image': 'courses/2020/06/python.jpg',
        'click_nums': '9',
        'course_org': '武汉大学',
        'tag': '4',
        'category': '专业课',
        'teacher': '',
    },
    {
        'name': 'c语言',
        'desc': 'c语言',
        'detail': 'C语言是一门面向过程的、抽象化的通用程序设计语言，广泛应用于底层开发。C语言能以简易的方式编译、处理低级存储器',
        'degree': 'cj',
        'learn_times': '3',
        'students': '11',
        'fav_nums': '36',
        'image': 'courses/2020/06/cyuyan.jpg',
        'click_nums': '76',
        'course_org': '大城小爱',
        'tag': '5',
        'category': '专业课',
        'teacher': '',
    },
    {
        'name': 'c语言',
        'desc': 'c语言',
        'detail': 'C语言是一门面向过程的、抽象化的通用程序设计语言，广泛应用于底层开发。C语言能以简易的方式编译、处理低级存储器',
        'degree': 'gj',
        'learn_times': '33',
        'students': '13',
        'fav_nums': '39',
        'image': 'courses/2020/06/cyuyan.jpg',
        'click_nums': '56',
        'course_org': '清华大学',
        'tag': '5',
        'category': '专业课',
        'teacher': '',
    },
    {
        'name': 'c语言',
        'desc': 'c语言',
        'detail': 'C语言是一门面向过程的、抽象化的通用程序设计语言，广泛应用于底层开发。C语言能以简易的方式编译、处理低级存储器',
        'degree': 'gj',
        'learn_times': '33',
        'students': '13',
        'fav_nums': '39',
        'image': 'courses/2020/06/cyuyan.jpg',
        'click_nums': '56',
        'course_org': '后古婚纱',
        'tag': '5',
        'category': '专业课',
        'teacher': '',
    },
    {
        'name': 'c语言',
        'desc': 'c语言',
        'detail': 'C语言是一门面向过程的、抽象化的通用程序设计语言，广泛应用于底层开发。C语言能以简易的方式编译、处理低级存储器',
        'degree': 'zj',
        'learn_times': '343',
        'students': '13',
        'fav_nums': '392',
        'image': 'courses/2020/06/cyuyan.jpg',
        'click_nums': '6',
        'course_org': '桔子摄影',
        'tag': '5',
        'category': '专业课',
        'teacher': '',
    },
    {
        'name': 'c语言',
        'desc': 'c语言',
        'detail': 'C语言是一门面向过程的、抽象化的通用程序设计语言，广泛应用于底层开发。C语言能以简易的方式编译、处理低级存储器',
        'degree': 'gj',
        'learn_times': '727',
        'students': '117',
        'fav_nums': '352',
        'image': 'courses/2020/06/cyuyan.jpg',
        'click_nums': '8',
        'course_org': '南京大学',
        'tag': '5',
        'category': '专业课',
        'teacher': '',
    },
    {
        'name': 'java',
        'desc': 'java',
        'detail': 'Java是一门面向对象编程语言，不仅吸收了C++语言的各种优点，还摒弃了C++里难以理解的多继承、指针等概念，因此Java语言具有功能强大和简单易用两个特征',
        'degree': 'gj',
        'learn_times': '26',
        'students': '97',
        'fav_nums': '58',
        'image': 'courses/2020/06/java.jpg',
        'click_nums': '853',
        'course_org': '南京大学',
        'tag': '6',
        'category': '专业课',
        'teacher': '',
    },
    {
        'name': 'java',
        'desc': 'java',
        'detail': 'Java是一门面向对象编程语言，不仅吸收了C++语言的各种优点，还摒弃了C++里难以理解的多继承、指针等概念，因此Java语言具有功能强大和简单易用两个特征',
        'degree': 'zj',
        'learn_times': '26',
        'students': '67',
        'fav_nums': '52',
        'image': 'courses/2020/06/java.jpg',
        'click_nums': '3',
        'course_org': '北京大学',
        'tag': '6',
        'category': '专业课',
        'teacher': '',
    },
    {
        'name': 'java',
        'desc': 'java',
        'detail': 'Java是一门面向对象编程语言，不仅吸收了C++语言的各种优点，还摒弃了C++里难以理解的多继承、指针等概念，因此Java语言具有功能强大和简单易用两个特征',
        'degree': 'cj',
        'learn_times': '294',
        'students': '65',
        'fav_nums': '79',
        'image': 'courses/2020/06/java.jpg',
        'click_nums': '99',
        'course_org': '厦门大学',
        'tag': '6',
        'category': '专业课',
        'teacher': '',
    },
    {
        'name': 'java',
        'desc': 'java',
        'detail': 'Java是一门面向对象编程语言，不仅吸收了C++语言的各种优点，还摒弃了C++里难以理解的多继承、指针等概念，因此Java语言具有功能强大和简单易用两个特征',
        'degree': 'gj',
        'learn_times': '735',
        'students': '103',
        'fav_nums': '728',
        'image': 'courses/2020/06/java.jpg',
        'click_nums': '19',
        'course_org': '新东方',
        'tag': '6',
        'category': '专业课',
        'teacher': '',
    },
    {
        'name': 'java',
        'desc': 'java',
        'detail': 'Java是一门面向对象编程语言，不仅吸收了C++语言的各种优点，还摒弃了C++里难以理解的多继承、指针等概念，因此Java语言具有功能强大和简单易用两个特征',
        'degree': 'gj',
        'learn_times': '95',
        'students': '86',
        'fav_nums': '63',
        'image': 'courses/2020/06/java.jpg',
        'click_nums': '39',
        'course_org': '卓越教育',
        'tag': '6',
        'category': '专业课',
        'teacher': '',
    },

]


def course():
    key_name = []
    for key in Course._meta.get_fields():
        try:
            if key.attname not in ['id', 'add_time', 'you_need_know', 'teacher_tell']:
                key_name.append(key.attname)
        except:
            pass

    for i in course_data:
        check = Course.objects.filter(
            Q(name=i['name']) & Q(course_org_id=CourseOrg.objects.get(name=i['course_org']).id))
        # check = Course.objects.filter(name=i['name'])
        if check:
            course = check
            for j in key_name:
                if j == 'course_org_id':
                    course[0].course_org_id = CourseOrg.objects.get(name=i['course_org']).id
                elif j == 'teacher_id':
                    course[0].teacher_id = Teacher.objects.get(name=i['teacher']).id
                else:
                    course[0].__setattr__(j, i[j])
            course[0].save()
        else:
            course = Course()
            for j in key_name:
                if j == 'course_org_id':
                    course.course_org_id = CourseOrg.objects.get(name=i['course_org']).id
                elif j == 'teacher_id':
                    course.teacher_id = Teacher.objects.get(name=i['teacher']).id
                else:
                    course.__setattr__(j, i[j])
            course.save()


lesson_data = [
    {'course': '1',
     'name': '第一章'},
    {'course': '1',
     'name': '第二章'},
    {'course': '1',
     'name': '第三章'},
    {'course': '1',
     'name': '第四章'},
    {'course': '1',
     'name': '第五章'}
]


def lesson():
    key_name = []
    for key in Lesson._meta.get_fields():
        try:
            if key.attname not in ['id', 'add_time']:
                key_name.append(key.attname)
        except:
            pass

    for i in lesson_data:
        check = Lesson.objects.filter(Q(name=i['name']) & Q(course_id=i['course']))
        if check:
            lesson = check
            for j in key_name:
                if j == 'course_id':
                    lesson[0].course_id = i['course']
                else:
                    lesson[0].__setattr__(j, i[j])
            lesson[0].save()
        else:
            lesson = Lesson()
            for j in key_name:
                if j == 'course_id':
                    lesson.course_id = i['course']
                else:
                    lesson.__setattr__(j, i[j])
            lesson.save()


if __name__ == '__main__':
    # city_dict()
    # course_org()
    # teacher()
    course()
    # lesson()
