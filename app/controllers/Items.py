# -*-coding:utf-8-*-
import numpy as np
import config
from app import app
from flask import request,render_template,flash,abort,url_for,redirect,session,Flask,g,jsonify


conn = config.conn
cursor = conn.cursor()


@app.route('/Items',methods=['GET','POST'])
def Items():
    return render_template('Items.html')


@app.route('/show_Items',methods=['GET','POST'])
def show_Items():
    layer=[]

    # 查询操作
    layer = queryModule(0)
    # 关闭连接
    conn.close()
    return jsonify( layer )


def queryModule(pk):
    sa=[]
    conn = config.conn
    cursor = conn.cursor()
    # sql = "select pk,FunValueEn,FunValueCn,FunOrder from FunModules where  Funlayer = %d ;"
    cursor.execute("select pk,FunValueEn,FunValueCn,FunOrder from FunModules where  Funlayer = %d" %(pk))
    row = cursor.fetchall()
    list = np.array(row).tolist()
    for l in list:
        if queryModule(int(l[0])):
            sa.append({"n":l[2],"s":queryModule(int(l[0]))})
        else:
            sa.append({"n": l[2]})
    return sa






