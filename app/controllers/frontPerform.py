# -*-coding:utf-8-*-
from flask import request,render_template,flash,abort,url_for,redirect,session,Flask,g,jsonify
from app.models.User import User

import os ,json,sys
from app import app,db
from datetime import date,timedelta
from sqlalchemy import extract
reload(sys)
sys.setdefaultencoding("utf-8")


# 定义路由index
@app.route('/frontPerform', methods=['GET', 'POST'])
def frontPerform():
    if request.method == 'POST':
        version = request.form.get("selected_version", "null")

    else:
        version = 'syf1.1.1'
    g.db = sqlite3.connect(config.db_dir)
    summary_data_sql = 'select page_name, url, dns, request, dom_parser, dom_ready, load_event, whitewait, loadall ' \
                       + " from WebLoad where version='" + str(version) + "'"
    page_load_result = query_db(summary_data_sql)

    g.db.close()
    project_version = config.project_version_info
    # 将页面信息转换为Echarts使用的数据
    page_chart_data = {}
    chart_list = []
    for value in ('page_name', 'loadall', 'dns', 'dom_ready', 'dom_parser', 'whitewait', 'request', 'load_event'):
        for webload in page_load_result:
            chart_list.append(webload[value])
            page_chart_data[value] = chart_list
        chart_list = []

    return render_template('index.html', project_version=project_version, page_load_result=page_load_result,
                           page_chart_data=page_chart_data)


# 定义重新执行脚本的路由
@app.route('/redo', methods=['GET', 'POST'])
def redo():
    if request.method == 'GET':
        return 'route does not support get'
    else:
        # 向测试环境发生get请求来验证测试环境是否存在
        env_for_test = request.form.get("selected_version", "null")
        current_env = config.hosts['164'] + env_for_test
        env_test_code = requests.get(current_env).status_code
        print  env_test_code
        if env_test_code == 200:
            # 定义页面名称列表
            all_page_data = {}
            page_urls = config.page_urls
            timing_js = config.timing_js

            # 统计页面加载时间的6个维度 登录页专用
            index_data = {'dns': 0, 'request': 0, 'dom_parser': 0, 'dom_ready': 0, 'load_event': 0, 'whitewait': 0,
                          'loadall': 0}
            # index页面资源的信息 登录页专用
            page_index_info = []
            # 将统计数据保存到sqlite
            connection = sqlite3.connect(config.db_dir)
            cursor = connection.cursor()
            # 先删除页面资源细分表webDetailLoad所有数据
            clear_resource_sql = "delete from PageDetail where project='Clinical' and version='" + env_for_test + "'"
            cursor.execute(clear_resource_sql)
            # 先清理上次的数据
            clear_webload_sql = "delete from WebLoad where project='Clinical' and version='" + env_for_test + "'"
            cursor.execute(clear_webload_sql)
            connection.commit()
            # get到clinical登录页(登录页需要单独收集其页面加载性能指标)
            driver = webdriver.Chrome()
            login_url = current_env + '/login/index'
            driver.get(login_url)
            driver.maximize_window()
            time.sleep(5)
            time_line = driver.execute_script(config.timing_js)
            # 将页面加载时间存入all_page_data
            for key in index_data.keys():
                index_data[key] = time_line[key]
            # 将index的数据存入all_page_data
            all_page_data['Index'] = index_data

            # 获得index页面所有的资源实体
            entries = driver.execute_script(config.get_entries_js)
            # 遍历登录页面所有资源
            for items in entries:
                # 以页面名：数组形式保存页面信息
                page_index_resource = {}
                # 资源名称
                page_index_resource['name'] = items['name']
                # 资源类型分类
                resource_type = str(items['name']).split('.')[-1]
                if resource_type in ['jpg', 'png', 'gif', 'jpeg']:
                    page_index_resource['resourceType'] = 'img'
                elif resource_type == 'js':
                    page_index_resource['resourceType'] = 'js'
                elif resource_type == 'css':
                    page_index_resource['resourceType'] = 'css'
                else:
                    if items['initiatorType'] == 'xmlhttprequest':
                        page_index_resource['resourceType'] = 'xmlhttprequest'
                    elif items['initiatorType'] == 'script':
                        page_index_resource['resourceType'] = 'js'
                    else:
                        page_index_resource['resourceType'] = 'other'
                # 资源大小
                page_index_resource['transferSize'] = items['transferSize']
                # 资源耗时
                page_index_resource['duration'] = items['duration']
                # 将登录页资源信息存入列表
                page_index_info.append(page_index_resource)
                # 将登录页资源列表信息存入字典对象 对应key为Index
                save_resource_sql = 'insert into PageDetail ' + "values('Clinical','" + str(
                    env_for_test) + "'," + "'" + str(
                    'Index') + "'," + "'" + str(page_index_resource['name']) + "'," + "'" + str(
                    page_index_resource['resourceType']) + "'," + "'" \
                                    + str(page_index_resource['transferSize']) + "'," + "'" + str(
                    page_index_resource['duration']) + "'," + 'CURRENT_TIMESTAMP)'
                cursor.execute(save_resource_sql)
                connection.commit()

            # 登录系统后 对其他所有页面进行遍历以收集其页面加载性能数据
            driver.find_element_by_id('txtUserName').send_keys('30048')
            driver.find_element_by_id('txtPassword').send_keys('5436')
            driver.find_element_by_id('btnConfirm').click()
            time.sleep(3)

            # 循环登录后的所有页面
            for page in page_urls.keys():
                # 将页面加载时间统计出来存入all_page_data
                current_page_timing = {"dns": 0, "request": 0, "dom_parser": 0, "dom_ready": 0, "load_event": 0,
                                       "whitewait": 0, "loadall": 0}
                current_page_url = current_env + (str(page_urls[page]))
                driver.get(current_page_url)
                time.sleep(10)
                durations = driver.execute_script(timing_js)
                for item in current_page_timing.keys():
                    current_page_timing[item] = durations[item]
                # 将当前页面的name和统计到数据存入到all_page_data
                all_page_data[page] = current_page_timing

                entries = driver.execute_script("return window.performance.getEntries()")
                # 遍历当前页面所有资源
                for items in entries:
                    current_resources = {}
                    current_resources['name'] = items['name']
                    # 根据资源类型进行统计
                    resource_type = str(items['name']).split('.')[-1]
                    if resource_type in ['jpg', 'png', 'gif', 'jpeg']:
                        current_resources['resourceType'] = 'img'
                    elif resource_type == 'js':
                        current_resources['resourceType'] = 'js'
                    elif resource_type == 'css':
                        current_resources['resourceType'] = 'css'
                    else:
                        if items['initiatorType'] == 'xmlhttprequest':
                            current_resources['resourceType'] = 'xmlhttprequest'
                        elif items['initiatorType'] == 'script':
                            current_resources['resourceType'] = 'js'
                        else:
                            current_resources['resourceType'] = 'other'
                    # 资源大小
                    current_resources['transferSize'] = items['transferSize']
                    # 资源耗时
                    current_resources['duration'] = items['duration']
                    # 保存资源
                    save_resource_sql = 'insert into PageDetail ' + "values('Clinical','" + str(
                        env_for_test) + "'," + "'" + str(
                        page) + "'," + "'" + str(
                        current_resources['name']) + "'," \
                                        + "'" + str(current_resources['resourceType']) + "'," + "'" + str(
                        current_resources['transferSize']) + "'," + "'" + str(
                        current_resources['duration']) + "'," + 'CURRENT_TIMESTAMP)'
                    cursor.execute(save_resource_sql)
                    connection.commit()
            # 退出chrome driver进程
            driver.quit()
            # 更新WebLoad表中的数据
            for name in all_page_data.keys():
                page_time = all_page_data[name]
                if name == 'Index':
                    insert_sql = 'insert into WebLoad ' + "values('Clinical','" + str(env_for_test) + "'," + "'" \
                                 + str(name) + "'," + "'" + str(current_env) + "/login/index'," + str(page_time['dns']) \
                                 + ',' + str(page_time['request']) + ',' + str(page_time['dom_parser']) + ',' + str(
                        page_time['dom_ready']) \
                                 + ',' + str(page_time['load_event']) + ',' + str(page_time['whitewait']) + ',' + str(
                        page_time['loadall']) + ',' + 'CURRENT_TIMESTAMP)'
                else:
                    insert_sql = 'insert into WebLoad ' + "values('Clinical','" + str(env_for_test) + "'," + "'" \
                                 + str(name) + "'," + "'" + str(current_env) + str(page_urls[name]) + "'," + str(
                        page_time['dns']) \
                                 + ',' + str(page_time['request']) + ',' + str(page_time['dom_parser']) + ',' + str(
                        page_time['dom_ready']) \
                                 + ',' + str(page_time['load_event']) + ',' + str(page_time['whitewait']) + ',' + str(
                        page_time['loadall']) + ',' + 'CURRENT_TIMESTAMP)'
                cursor.execute(insert_sql)
                connection.commit()
            connection.close()

            return 'success'
        else:
            return 'environment is not exist'


@app.route('/detail_<project_version>_<page_name>')
def page_detail(project_version, page_name):
    g.db = sqlite3.connect(config.db_dir)
    # 页面资源信息
    resource_sql = "select resource_name, resource_type, resource_size, resource_duration from PageDetail where version='" + str(
        project_version) + "' and page_name='" + str(page_name) + "'"

    history_sql = "select version, dns, request, dom_parser, dom_ready, load_event, whitewait, loadall from WebLoad where page_name='" + str(
        page_name) + "' group by version"
    composition_sql = "select resource_type, count(resource_type) as counts, sum(resource_size) as size_count, sum(resource_duration) as duration_count from PageDetail where version='" + str(
        project_version) + "' and page_name='" + str(page_name) + "' group by resource_type"
    top_sql = "select resource_name, resource_duration, resource_size from PageDetail where version='" + str(
        project_version) + "' and page_name='" + str(page_name) + "' order by resource_duration desc limit 3"
    resource_composition = query_db(composition_sql)
    resource_summary = query_db(resource_sql)

    top_resources = query_db(top_sql)
    # 对历史数据比对来说 若只有一个版本需要添加默认的比对数据
    history_info = query_db(history_sql)
    g.db.close()
    if len(history_info) > 1:
        pass
    else:
        default_data = {'version': 'syf-next-version', 'dns': 0, 'request': 0, 'dom_parser': 0, 'dom_ready': 0,
                        'load_event': 0, 'whitewait': 0, 'loadall': 0}
        history_info.append(default_data)
    version_list = []
    for data in history_info:
        version_list.append(str(data['version']).strip("u"))

    resource_type_list = []
    for item in resource_composition:
        resource_type_list.append(item['resource_type'])
    return render_template('page_detail.html', resource_summary=resource_summary, history_info=history_info,
                           page_name=page_name,
                           version_list=version_list, resource_composition=resource_composition,
                           resource_type_list=resource_type_list,
                           top_resources=top_resources)


@app.route('/ui_auto', methods=['GET', 'POST'])
def ui_auto():
    if request.method == 'POST':
        version = request.form.get("selected_version", "null")
    else:
        version = 'Syf1.1.1'
    g.db = sqlite3.connect(config.db_dir)
    g.db.text_factory = str
    testSuites_sql = 'select testsuitename,subsuite,totalcase,passedcase,failedcase, duration from TestSuite' + " where projectname ='" + str(
        version) + "'"
    testSuites = query_db(testSuites_sql)

    # testSuites = testSuites.encode('utf-8')
    # print testSuites[0]['testsuitename'].encode('gb2312','ignore')

    g.db.close()
    project_version = config.project_version_info

    return render_template('ui_auto.html', project_version=project_version, testSuites=testSuites)


# ui自动化执行
@app.route('/uitest_operate', methods=['POST'])
def uitest_operate():
    # 验证是测试环境是否存在该版本号
    env_for_test = request.form.get("select_version", "null")
    testsuite = request.form.get("testsuite", "null")
    subsuite = request.form.get("subsuite", "null")
    current_env = config.hosts['164'] + env_for_test
    env_test_code = requests.get(current_env).status_code
    print env_for_test, testsuite, subsuite, env_test_code
    if env_test_code == 200:
        try:
            file_name = config.ui_suites_dir + '\\' + env_for_test + '\\' + str(testsuite) + '\\'
            test_name = str(subsuite) + '.txt'

            print file_name
            command_line = "pybot %s" % test_name
            process = subprocess.Popen(command_line, shell=True, cwd=file_name)
            retcode = process.wait()
        except Exception as e:
            raise e
        return 'seccess'
    else:
        return 'environment is not exist'


@app.route('/service_auto')
def service_auto():
    return render_template('service_auto.html')


@app.route('/case_detail')
def case_detail():
    return render_template('case_detail.html')


@app.route('/cap_auto')
def cap_auto():
    return render_template('cap_auto.html')


@app.route('/per_auto')
def per_auto():
    return render_template('per_auto.html')


@app.route('/savetodo', methods=['GET', 'POST'])
def savetodo():
    if request.method == 'POST':
        rid = request.form.get("id", "null")
        project = request.form.get("project", "null")
        version = request.form.get("version", "null")
        worktype = request.form.get("worktype", "null")
        module = request.form.get("module", "null")
        title = request.form.get("title", "null")
        description = request.form.get("description", "null")
        developer = request.form.get("developer", "null")
        tester = request.form.get("tester", "null")
        status = request.form.get("status", "null")
        createtime = request.form.get("createtime", "null")
        completetime = request.form.get("completetime", "null")
        remarks = request.form.get("remarks", "null")
        CURRENT = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        # 将统计数据保存到sqlite

        connection = sqlite3.connect(config.db_dir)
        cursor = connection.cursor()

        save_sql = "insert into todolist values ('" + str(rid) + "','" + str(project) + "','" + str(
            version) + "','" + str(worktype) + "','" + str(module) + "',\
        '" + str(title) + "','" + str(description) + "','" + str(developer) + "','" + str(tester) + "','" + str(
            status) + "','" + str(createtime) + "','" + str(completetime) + "','" + str(remarks) + "','" + str(
            CURRENT) + "')"
        cursor.execute(save_sql)
        connection.commit()
        connection.close()
        # 重新读取数据库的信息
        g.db = sqlite3.connect(config.db_dir)
        g.db.text_factory = str

        select_sql = 'select rid,version,worktype,module,title,description,developer,tester,status,createtime,completetime,remarks ' \
                     + "from todolist where project='" + str(project) + "'"
        todolists = query_db(select_sql)
        g.db.close()
        return render_template('todo.html', todolists=todolists)



# 以字典形式返回查询结果
def query_db(query, args=(), one=False):
    cur = g.db.execute(query, args)
    rv = [dict(
        (str(cur.description[idx][0]), str(value).replace("\n", "<br/>").replace("\r", "<br/>")) for idx, value in
        enumerate(row)) for row in cur.fetchall()]
    return (str(rv[0]) if rv else None) if one else rv


# 全局环境变量配置
@app.route('/variable_config', methods=['GET', 'POST'])
def variable_config():
    if request.method == 'GET':
        return render_template('variable_config.html')
    else:
        return render_template('variable_config.html')


@app.route('/bootstrap-tabletest', methods=['GET', 'POST'])
def bootstraptabletest():
    userlists = [{"UserName": "张三", "Age": 22, "Birthday": "1994-12-21", "DeptId": "1", "DeptName": "研发部"}, \
                 {"UserName": "李四", "Age": 28, "Birthday": "1988-09-09", "DeptId": "2", "DeptName": "销售部"}, \
                 {"UserName": "风衣大叔", "Age": 40, "Birthday": "1976-09-01", "DeptId": "2", "DeptName": "销售部"}]
    return render_template('bootstraptabletest.html', userlists=userlists)