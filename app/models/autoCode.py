# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String, Unicode,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,relationship,backref
from sqlalchemy.orm import scoped_session
import re

engine = create_engine("mssql+pymssql://mduser:mduser@192.168.10.244/AutoCodeDB2", encoding='utf-8', echo=True)
Base = declarative_base()
metadata = Base.metadata
DBSession = sessionmaker(bind=engine)


class FunItemList(Base):   #child
    __tablename__ = 'FunItemList'

    Pk = Column(Integer, primary_key=True)
    FunItemsFk = Column(String(360, u'Chinese_PRC_CI_AS'),nullable=False)
    ItemValueEn = Column(Unicode)
    ItemValueCn = Column(Unicode)
    ItemTitle = Column(Unicode)
    ItemOrder = Column(Integer)
    CreatedTime = Column(DateTime, nullable=False)
    DropDownboxKey = Column(Unicode,ForeignKey('FunItems.DropDownbox'))


    def __repr__(self):
        return '<FunItemList ItemValueCn:%r ItemTitle:%r >\n' %(self.ItemValueCn, self.ItemTitle)

    def __init__(self,FunItemsFk,ItemValueEn,ItemValueCn,ItemTitle,ItemOrder,CreatedTime,DropDownboxKey):
        self.FunItemsFk = FunItemsFk
        self.ItemValueEn = ItemValueEn
        self.ItemValueCn = ItemValueCn
        self.ItemTitle = ItemTitle
        self.ItemOrder = ItemOrder
        self.CreatedTime = CreatedTime
        self.DropDownboxKey = DropDownboxKey

    def to_json(self):
        return {
            'Pk': self.Pk,
            'FunItemsFk': self.FunItemsFk,
            'ItemValueEn': self.ItemValueEn,
            'ItemValueCn': self.ItemValueCn,
            'ItemTitle': self.ItemTitle,
            'ItemOrder': self.ItemOrder,
            'CreatedTime': self.CreatedTime,
            'DropDownboxKey':self.DropDownboxKey

        }


class FunItem(Base):                 #parent
    __tablename__ = 'FunItems'

    Pk = Column(String(360, u'Chinese_PRC_CI_AS'), primary_key=True)
    FunModulesFk = Column(Integer,nullable=False)
    FunItemKey = Column(Unicode(500))
    FunItemValueEn = Column(Unicode(500))
    FunItemValueCn = Column(Unicode(500))
    FunItemTitle = Column(Unicode(500))
    FunItemHtmlType = Column(Unicode(50))
    FunItemDbType = Column(Unicode(50))
    DefaultVal = Column(Unicode(50))
    FunItemOrder = Column(Integer)
    DropDownbox = Column(Unicode(50))
    OpenSelectKey = Column(Unicode(50))
    CreatedTime = Column(DateTime, nullable=False)
    DerivedRuleDec = Column(Unicode)
    FunItemOrder2 = Column(Integer, nullable=False)
    ObjData = Column(Unicode)
    FieldIdentifier = Column(Unicode(50))
    dropdownMenus = relationship('FunItemList',backref="FunItems")


    def __repr__(self):
        return '<FunItem FunItemValueCn:%r FunItemTitle:%r >\n' %(self.FunItemValueCn, self.FunItemTitle)

    def __init__(self, Pk, FunModulesFk, FunItemKey,FunItemValueEn,FunItemValueCn,FunItemTitle,\
                 FunItemHtmlType,FunItemDbType,DefaultVal,FunItemOrder,DropDownbox,CreatedTime,\
                 DerivedRuleDec,FunItemOrder2,ObjData,FieldIdentifier,OpenSelectKey):
        self.Pk = Pk
        self.FunModulesFk = FunModulesFk
        self.FunItemKey = FunItemKey
        self.FunItemValueEn = FunItemValueEn
        self.FunItemValueCn = FunItemValueCn
        self.FunItemTitle = FunItemTitle
        self.FunItemHtmlType = FunItemHtmlType
        self.FunItemDbType = FunItemDbType
        self.DefaultVal = DefaultVal
        self.FunItemOrder = FunItemOrder
        self.DropDownbox = DropDownbox
        self.CreatedTime = CreatedTime
        self.DerivedRuleDec = DerivedRuleDec
        self.FunItemOrder2 = FunItemOrder2
        self.ObjData = ObjData
        self.FieldIdentifier = FieldIdentifier
        self.OpenSelectKey = OpenSelectKey

    def to_json(self):
        return {
            'Pk': self.Pk,
            'FunModulesFk': self.FunModulesFk,
            'FunItemKey': self.FunItemKey,
            'FunItemValueEn': self.FunItemValueEn,
            'FunItemValueCn': self.FunItemValueCn,
            'FunItemTitle': self.FunItemTitle,
            'FunItemHtmlType': self.FunItemHtmlType,
            'FunItemDbType': self.FunItemDbType,
            'DefaultVal': self.DefaultVal,
            'FunItemOrder': self.FunItemOrder,
            'DropDownbox': self.DropDownbox,
            'CreatedTime': self.CreatedTime,
            'DerivedRuleDec': self.DerivedRuleDec,
            'FunItemOrder2': self.FunItemOrder2,
            'ObjData': self.ObjData,
            'FieldIdentifier': self.FieldIdentifier,
            'OpenSelectKey':self.OpenSelectKey,
            'dropdownMenus': self.get_dropdownMenus(),
            'dropdownKey':self.get_dropdownKeys()
        }

    def get_DerivedRuleDec(self):
        if self.DerivedRuleDec:
            pattern = r"(\<.*?\>)"
            return self.DerivedRuleDec.re(pattern,self.DerivedRuleDec)
    def get_dropdownMenus(self):
        dropdownMenus = []
        if self.dropdownMenus:
            for menu in self.dropdownMenus:
                menu.to_json()
                dropdownMenus.append(menu.ItemValueCn + '[' + menu.ItemTitle + ']')
        return dropdownMenus

    def get_dropdownKeys(self):
        dropdownKeys = []
        if self.dropdownMenus:
            for menu in self.dropdownMenus:
                menu.to_json()
                if(menu.DropDownboxKey not in dropdownKeys):
                    dropdownKeys.append(menu.DropDownboxKey)
        return dropdownKeys

    def to_dict(self):
        return dict([(k, getattr(self, k)) for k in self.__dict__.keys() if not k.startswith("_")])




class FunModule(Base):
    __tablename__ = 'FunModules'

    Pk = Column(Integer, primary_key=True)
    FunValueEn = Column(Unicode(500))
    FunValueCn = Column(Unicode(500))
    FunTitle = Column(Unicode(500))
    FunOrder = Column(Integer)
    FunLayer = Column(Integer, nullable=False)
    CreatedTime = Column(DateTime, nullable=False)
    ObjData = Column(Unicode)


    def __repr__(self):
        return '<FunModule FunValueCn:%r FunLayer:%r >\n' %(self.FunValueCn, self.FunLayer)

    def __init__(self, Pk, FunValueEn,FunValueCn,FunTitle,FunOrder,FunLayer,CreatedTime,ObjData):
        self.Pk = Pk
        self.FunValueEn = FunValueEn
        self.FunValueCn = FunValueCn
        self.FunTitle = FunTitle
        self.FunOrder = FunOrder
        self.FunLayer = FunLayer
        self.CreatedTime = CreatedTime
        self.ObjData = ObjData

    def to_json(self):
        return {
            'Pk': self.Pk,
            'FunValueEn': self.FunValueEn,
            'FunValueCn': self.FunValueCn,
            'FunTitle': self.FunTitle,
            'FunOrder': self.FunOrder,
            'FunItemTitle': self.FunItemTitle,
            'FunOrder': self.FunOrder,
            'FunLayer': self.FunLayer,
            'CreatedTime': self.CreatedTime,
            'ObjData': self.ObjData,

        }


    def to_dict(self):
        return dict([(k, getattr(self, k)) for k in self.__dict__.keys() if not k.startswith("_")])


class PopUpMenu(Base):
    __tablename__ = 'PopUpMenu'

    Pk = Column(Unicode(36), primary_key=True)
    MenuType = Column(Integer)
    MenuKey = Column(Unicode(500))
    MenuName = Column(Unicode(500))
    MenuCode = Column(Unicode)
    ObjData = Column(Unicode)
