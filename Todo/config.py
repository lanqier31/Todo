# -#-coding:utf-8 -*-
import os
import pymssql
basedir = os.path.abspath(os.path.dirname(__file__))
db_dir = os.path.join(basedir, 'app.db')
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')    #数据库文件的路径
#SQLALCHEMY_MIGRATE_REPO 是文件夹，我们将会把 SQLAlchemy-migrate 数据文件存储在这里
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_COMMIT_ON_TEARDOWN = True   #该配置为True,则每次请求结束都会自动commit数据库的变动
CSRF_ENBLE = True                     #激活站点请求伪造保护
SECRET_KEY = 'YOU-Will-never-guess'   #仅仅当CSRF激活是才需要，用于建立加密令牌，验证表单

# 定义UI自动化上传文件存放路径
ui_suites_dir = os.path.join(basedir, 'Web\ui_suites')
# 定义所有页面
page_urls = \
    {
        "SelectSystem": "/Login/SelectSystem",
        "AppointsSummary": "/Main/Order",      #预约图表页
        "AppointList": "/ReferralAppointment/ReferralAppointmentList",   #预约列表页
        "LostManage": "/lost/lostmanage" ,
        "PatientManage" : "/patient/patientmanage",
        "MainAnalysis": "/main/analysis",            #预约管理统计分析
        "reportList":"/SyfHospitalClinicalDataCenter/index",          #报告类别页面
        "reportManage":"/SyfHospitalClinicalDataCenter/QueryReport?type=add&hospitalNumber=2443605&editmark=true",
        "ComplexcheckEvaluation":"/ComplexcheckEvaluation/Edit?pk=8007d6d8-c127-4bfc-9d86-fed87f8d19ba",
        "PathologicalEvaluation":"/PathologicalEvaluation/Edit?type=add&editmark=true&hno=2443605&target=report&d=Fri%20May%2004%202018%2014:03:52%20GMT+0800%20(%D6%D0%B9%FA%B1%EA%D7%BC%CA%B1%BC%E4)&reportdate=2015-10-19",
        "YearpointTest2":"/YearpointTest2/Edit?type=add&editmark=false&hospitalNumber=2443605&target=report&nq=2&reportdate=2015-10-19"
        # "UsersManage": "/systemset/usersetting",
        # "RolesSetting": "/systemset/rolesetting",
        # "DepartmentSetting": "/systemset/departmentsetting",
        # "AdmissionConfig": "/systemset/AdmissionConfig",  #预约管理诊日设置
        # "UserDateList": "/systemset/UserDateList",
        # "ConfigSetting": "/SystemSet/ConfigSetting",
        # "BasicSetting": "/SystemSet/BasicSetting",
        # "SysLog": "/SysLog/Index",
        # "TumorSummary": "/TumorStudy2/Order",                                       #术后状态页
        # "TumorList": "/TumorStudy2/Index",                                          #术后列表页
        # "TumorAdd": "/PathologicalEvaluation/Edit?type=add&editmark=true",
        # "EvaluationSummary": "/ComplexcheckEvaluation/Order",
        # "EvaluationList": "/ComplexcheckEvaluation/Index",
        # "EvaluationAdd": "/ComplexcheckEvaluation/Edit?type=add&editmark=true",
        # "YearPoint": "/YearpointTest2/Order",
        # "YearPointList": "/YearpointTest2/Index",
        # "YearPointAdd": "/YearpointTest2/Edit?type=add&editmark=true"

    }

# 定义监控前端加载数据的js
timing_js = "{var performance = window.performance;\
            if (!performance) {\
            console.log('page time in durations');\
            return;\
            }\
            var t = performance.timing;\
            var times = {};\
            times.dns = (t.domainLookupEnd - t.domainLookupStart)/1000;\
            times.request = (t.responseEnd - t.requestStart)/1000;\
            times.dom_parser = (t.domComplete - t.domInteractive)/1000;\
            times.redirect = (t.redirectEnd - t.redirectStart)/1000;\
            times.dom_ready = (t.domContentLoadedEventEnd - t.navigationStart)/1000;\
            times.load_event = (t.loadEventEnd - t.loadEventStart)/1000;\
            times.whitewait = (t.domLoading  - t.navigationStart)/1000;\
            times.ttfb = (t.responseStart - t.navigationStart)/1000;\
            times.loadall = (t.loadEventEnd - t.navigationStart)/1000; \
            return times;}"
# 定义获得页面资源的方法
get_entries_js = 'return window.performance.getEntries()'

# 定义项目及其版本信息
project_version_info = {'Syf':['syf1.1.1', 'syf1.2.0', 'syf1.3.0'], 'DicomStorage': ['2.8.8', '2.8.9', '2.8.10'], 'Training': ['1.6.16', '1.6.17']}

# 定义测试机
hosts = {'localhost': 'http://127.0.0.1/', '164': 'http://192.168.10.164/', '243':'http://192.168.10.243/'}

#定义sqlserver连接

# conn = pymssql.connect('192.168.10.244', 'mduser', 'mduser', 'AutoCodeDB2')

