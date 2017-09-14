#coding=utf-8
from appiumframework.PO import base_page
import time

class LoginPage(base_page.Action):
    pwlogin_botton_loc = ("com.meipingmi.manager:id/tv_pwd_login")
    et_phone_loc = ("com.meipingmi.manager:id/et_phone")
    et_pwd_loc = ("com.meipingmi.manager:id/et_pwd")
    login_botto_loc = ('com.meipingmi.manager:id/btn_login')

    def login_button_link(self):
        self.find_element(self.pwlogin_botton_loc).click()
        time.sleep(3)           #点击密码登录

    def run_case1(self,value):
        self.find_element(self.et_phone_loc).send_keys(value)
        time.sleep(5)          #输入手机号码

    def run_case2(self, value):
        self.find_element(self.et_pwd_loc).send_keys(value)
        time.sleep(2)    #输入密码
        self.find_element(self. login_botto_loc).click()
        time.sleep(2)    #点击登录按钮
