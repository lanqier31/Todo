# -*-coding:utf-8-*-
import numpy as np
import config
from app import app
from flask import request,render_template,flash,abort,url_for,redirect,session,Flask,g,jsonify
from app.models.autoCode import FunItemList,FunItem,FunModule,PopUpMenu,DBSession

session = DBSession()


@app.route('/Items',methods=['GET','POST'])
def Items():
    return render_template('Items.html')


@app.route('/show_Items',methods=['GET','POST'])
def show_Items():
    layer=[]
    # 查询操作
    layer = queryModule(0)

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
            sa.append({"n":l[2],"value":int(l[0]),"s":queryModule(int(l[0]))})
        else:
            sa.append({"n": l[2],"value":int(l[0])})

    return sa
    # 关闭连接
    conn.close()


@app.route('/query_Items',methods=['GET','POST'])
def query_Items():
    try:
        Items = []
        limit = request.args.get('limit')
        offset = request.args.get('offset')
        menu1 = request.args.get('menu1')
        menu2 = request.args.get('menu2')
        menu3 = request.args.get('menu3')
        menu4 = request.args.get('menu4')
        menu5 = request.args.get('menu5')
        menu6 = request.args.get('menu6')
        if menu6:
            itemlist = session.query(FunItem).filter_by(FunModulesFk=menu6).order_by(FunItem.FunItemOrder.asc()).all()
        elif menu5:
            itemlist = session.query(FunItem).filter_by(FunModulesFk=menu5).order_by(FunItem.FunItemOrder.asc()).all()
        elif menu4:
            itemlist = session.query(FunItem).filter_by(FunModulesFk=menu4).order_by(FunItem.FunItemOrder.asc()).all()
        elif menu3:
            itemlist = session.query(FunItem).filter_by(FunModulesFk=menu3).order_by(FunItem.FunItemOrder.asc()).all()
        elif menu2:
            itemlist = session.query(FunItem).filter_by(FunModulesFk=menu2).order_by(FunItem.FunItemOrder.asc()).all()
        else:
            itemlist = session.query(FunItem).filter_by(FunModulesFk=menu1).order_by(FunItem.FunItemOrder.asc()).all()

        total = len(itemlist)

        for i in itemlist:
            Items.append(i.to_json())
        return jsonify({"total": total, 'rows': Items[int(offset):(int(offset) + int(limit))]})

    except IOError:
        return "error"


