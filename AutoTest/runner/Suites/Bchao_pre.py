#!/usr/bin/env python
# -*-coding:utf-8 -*-
# Author:  Weir Gao --<>
# Purpose:首次术前的B超校验
# Created: 2019/3/05


import sys
import os
from config import baseconf
from src.common.LoginPage import  LoginPage
from src.common.ClinicalReport import ClinicalReport
from src.common import opexcel

#we use global varialbe driver
# driver=Config.ChromeDriver
#Url for login is a global varible
url=baseconf.LoginUrl
login= LoginPage()
login.login_syf(url, '30048', '5579')
HospitalNums = opexcel.All_content('Hid')

for Hid in HospitalNums:   #遍历要测试的病历号
    login.goto_Report()
    dd = ClinicalReport()
    dd.input_Hid(Hid)
    dd.jiaoyan('Bchao_pre',Hid)
