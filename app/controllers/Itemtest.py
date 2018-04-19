# -*-coding:utf-8-*-

from app.models.autoCode import FunItemList,FunItem,FunModule,PopUpMenu,DBSession

session = DBSession()

items = session.query(FunModule).filter_by(FunLayer=0).all()
print items[1].Pk

