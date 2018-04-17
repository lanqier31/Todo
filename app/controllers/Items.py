# -*-coding:utf-8-*-
import pymssql

# server    数据库服务器名称或IP
# user      用户名
# password  密码
# database  数据库名称
conn = pymssql.connect('192.168.10.244', 'mduser', 'mduser', 'AutoCodeDB')

cursor = conn.cursor()


# 查询操作
cursor.execute('SELECT FunValueCn FROM FunModules WHERE Funlayer=0;')
row = cursor.fetchone()
while row:
    print row
    # print("ID=%d, Name=%s" % (row[0], row[1]))
    row = cursor.fetchone()

# 也可以使用for循环来迭代查询结果
# for row in cursor:
#     print("ID=%d, Name=%s" % (row[0], row[1]))

# 关闭连接
conn.close()