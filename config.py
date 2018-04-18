# -#-coding:utf-8 -*-
import os
import pymssql
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')    #数据库文件的路径
#SQLALCHEMY_MIGRATE_REPO 是文件夹，我们将会把 SQLAlchemy-migrate 数据文件存储在这里
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
CSRF_ENBLE = True                     #激活站点请求伪造保护
SECRET_KEY = 'YOU-Will-never-guess'   #仅仅当CSRF激活是才需要，用于建立加密令牌，验证表单
OPENID_PROVIDERS=[
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}
]



# 定义UI自动化上传文件存放路径
ui_suites_dir = os.path.join(basedir, 'Web\ui_suites')
# 定义所有页面
page_urls = \
    {
        "SelectSystem": "/Login/SelectSystem",
        "AppointsSummary": "/Main/Order",
        "AppointList": "/ReferralAppointment/ReferralAppointmentList",
        "LostManage": "/lost/lostmanage" ,
        "PatientManage" : "/patient/patientmanage",
        "SmsIndex": "/SMS/Index",
        "MainAnalysis": "/main/analysis",
        "UsersManage": "/systemset/usersetting",
        "RolesSetting": "/systemset/rolesetting",
        "DepartmentSetting": "/systemset/departmentsetting",
        "AdmissionConfig": "/systemset/AdmissionConfig",
        "UserDateList": "/systemset/UserDateList",
        "ConfigSetting": "/SystemSet/ConfigSetting",
        "BasicSetting": "/SystemSet/BasicSetting",
        "SysLog": "/SysLog/Index",
        "TumorSummary": "/TumorStudy2/Order",
        "TumorList": "/TumorStudy2/Index",
        "TumorAdd": "/PathologicalEvaluation/Edit?type=add&editmark=true",
        "EvaluationSummary": "/ComplexcheckEvaluation/Order",
        "EvaluationList": "/ComplexcheckEvaluation/Index",
        "EvaluationAdd": "/ComplexcheckEvaluation/Edit?type=add&editmark=true",
        "YearPoint": "/YearpointTest2/Order",
        "YearPointList": "/YearpointTest2/Index",
        "YearPointAdd": "/YearpointTest2/Edit?type=add&editmark=true"

    }

# 定义监控前端加载数据的js
timing_js = "{var performance = window.performance;\
            if (!performance) {\
            console.log('page time in durations');\
            return;\
            }\
            var t = performance.timing;\
            var times = {};\
            times.dns = t.domainLookupEnd - t.domainLookupStart;\
            times.request = t.responseEnd - t.requestStart;\
            times.dom_parser = t.domComplete - t.domInteractive;\
            times.redirect = t.redirectEnd - t.redirectStart;\
            times.dom_ready = t.domContentLoadedEventEnd - t.navigationStart;\
            times.load_event = t.loadEventEnd - t.loadEventStart;\
            times.whitewait = t.domLoading  - t.navigationStart;\
            times.ttfb = t.responseStart - t.navigationStart;\
            times.loadall = t.loadEventEnd - t.navigationStart; \
            return times;}"
# 定义获得页面资源的方法
get_entries_js = 'return window.performance.getEntries()'

# 定义项目及其版本信息
project_version_info = {'Clinical':['syf1.1.1', 'syf2.0.0', 'syf3.0.0'], 'DicomStorage': ['2.8.8', '2.8.9', '2.8.10'], 'Training': ['1.6.16', '1.6.17']}

# 定义测试机
hosts = {'localhost': 'http://127.0.0.1/', '164': 'http://192.168.10.164/'}

#定义sqlserver连接

conn = pymssql.connect('192.168.10.244', 'mduser', 'mduser', 'AutoCodeDB')

