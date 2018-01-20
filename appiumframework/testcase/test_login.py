#coding=utf-8
_author_ = "Maoge"

from appium import webdriver
import unittest
#from appiumframework.PO.login_page import CreatPage
import time
import threading
import xlrd,xlwt,xlutils
from xlutils.copy import copy
import datetime,subprocess

from appiumframework.PO.login_page import LoginPage
from appiumframework.PO.sysetting_page import SettingPage

class Test(unittest.TestCase):
    """自动化"""
    def setUp(self):
        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'Android Emulator',#可有可无
            'platformVersion': '5.0',

            # apk包名
            'appPackage': 'com.meipingmi.manager',
            # apk的launcherActivity
            'appActivity': 'com.meipingmi.manager.base.WelcomeActivity',
            #如果存在activity之间的切换可以用这个
            # 'appWaitActivity':'.MainActivity',
            'unicodeKeyboard': True,
            #隐藏手机中的软键盘
            'resetKeyboard': True
            }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        time.sleep(5)





    def tearDown(self):
        self.driver.quit()

    def test_loginpwd(self):
        """密码登录"""
        sp = LoginPage(self.driver)
        sp.login_button_link()
        sp.run_case1('13805728638')
        sp.run_case2('gjm123')



    def test_setting(self):
        """系统设置"""
        time.sleep(5)
        sp = SettingPage(self.driver)
        sp.setting_botton_link()
        sp.run_case('')

        #修改密码
        sp.run_updatapwd('gjm123')
        sp.run_newpwd('gjm147')
        sp.run_confirm_newpwd('gjm147')
        sp.login_button_link()
        sp.run_case1('13805728638')
        sp.run_case2('gjm147')




