# -*-coding:utf-8-*-
# import numpy as np
import config
from app import app
from flask import request,render_template,flash,abort,url_for,redirect,session,Flask,g,jsonify
from app.models.autoCode import FunItemList,FunItem,FunModule,PopUpMenu,DBSession
import re , sys  #正则表达式
from datetime import date,datetime
session = DBSession()
reload(sys)
sys.setdefaultencoding("utf-8")


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


def queryModule1(pk):
    sa=[]
    modules = session.query(FunModule).filter_by(FunLayer=pk).all()

    for m in modules:
        if queryModule(int(m.Pk)):
            sa.append({"n":m.FunValueCn,"value":int(m.Pk),"s":queryModule(int(m.Pk))})
        else:
            sa.append({"n": m.FunValueCn,"value":int(m.Pk)})

    return sa


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

    except:
        session.rollback()
        return "error"


@app.route('/edit_Item',methods=['GET','POST'])
def edit_Item():
    try:
        Pk = request.form.get("Pk", "null")
        field = request.form.get("name", "null")
        value = request.form.get("value", 'null')
        dropdownMenus = request.form.getlist('dropdownMenus[]')
        dropdownKey = request.form.get("dropDownKey", 'null')
        funItem = session.query(FunItem).filter_by(Pk=Pk).first()

        if(field == 'DerivedRuleDec'):
            funItem.DerivedRuleDec = value
        if (field == 'DropDownbox'):
            dropmenus=[]
            titles = []
            itemlist=session.query(FunItemList).filter_by(DropDownboxKey=value).all()
            if(itemlist):      #获取该key下面的所有下拉菜单
                for item in itemlist:
                    dropmenus.append(item.ItemValueCn)
                    titles.append(item.ItemTitle)
            else:          #如果该Key之前没绑定过下拉菜单，则默认将现有下拉菜单的内容赋值给该下拉菜单
                for v in dropdownMenus:
                    dropmenus.append( str(v).split('[')[0])
                    title = re.findall(r"(\[.*?\])", v, re.M)
                    if (len(title) > 0):
                        title = title[0]
                    titles.append(title.replace('[', '').replace(']', ''))

            """删除所有的跟该PK相关的funItemList，对下来菜单进行重新赋值"""
            itemList = session.query(FunItemList).filter_by(FunItemsFk=Pk).all()
            for list in itemList:
                session.delete(list)
            session.commit()
            for i in range(0,len(dropmenus)):
                itemlist = FunItemList(FunItemsFk=Pk, ItemValueEn=None, ItemValueCn=unicode(dropmenus[i]), ItemTitle=unicode(titles[i]),
                                       ItemOrder=i+1, CreatedTime=datetime.now(),DropDownboxKey=value)
                session.add(itemlist)
                session.commit()
            #给funItem这个字段绑定下拉菜单的值
            funItem.DropDownbox = value

        if(field == 'FunItemValueCn'):
            funItem.FunItemValueCn = value
        if(field == 'OpenSelectKey'):
            funItem.OpenSelectKey = value
        if(field == 'dropdownMenus'):
            #当DropdownMenu不为空时，判断DropdownKey不能为空
            if(value) and not (dropdownKey):
                return "KeyError"
            else:
                #删除现有绑定的下拉菜单

                itemList = session.query(FunItemList).filter_by(DropDownboxKey=dropdownKey).all()
                for list in itemList:
                    session.delete(list)
                session.commit()
                if (value):
                    value= value.split('\n')
                    i=1
                    for v in value:
                        dropMenu = v.split('[')[0]
                        title = re.findall(r"(\[.*?\])", v, re.M)
                        if (len(title) > 0):
                            title = title[0]
                        title = title.replace('[', '').replace(']', '')
                        cur = datetime.now()
                        itemlist= FunItemList(FunItemsFk=Pk,ItemValueEn=None,ItemValueCn=dropMenu,ItemTitle=title,ItemOrder=i,CreatedTime=cur,DropDownboxKey=dropdownKey)
                        session.add(itemlist)
                        session.commit()
                        i=i+1

        session.add(funItem)
        session.commit()
        return 'success'
    except:
        session.rollback()
        return "error"