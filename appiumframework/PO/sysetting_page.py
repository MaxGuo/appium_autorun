#coding=utf-8
_author_ = "Maoge"
from appiumframework.PO import base_page
import time

class SettingPage(base_page.Action):
    setting_botton_loc = ("com.meipingmi.manager:id/tv_settings")
    about_loc = ("com.meipingmi.manager:id/about_app")
    update_pwd_loc = ("com.meipingmi.manager:id/pwd_change")
    loginout_botto_loc = ('com.meipingmi.manager:id/btn_exit')
    checkversion_botto_loc = ('com.meipingmi.manager:id/tv_version_update')
    back_botto_loc = ('com.meipingmi.manager:id/back')
    old_pwd_loc = ('com.meipingmi.manager:id/et_old_pwd')
    new_pwd_loc = ('com.meipingmi.manager:id/et_new_pwd_confirm')
    new_pwd_confirm_loc = ('com.meipingmi.manager:id/et_new_pwd')
    confirm_botton_loc = ('com.meipingmi.manager:id/btn_confirm')
    exit_botton_loc = ('com.meipingmi.manager:id/btn_exit')
    exit_no_botton_loc = ('android:id/button2')
    exit_yes_botton_loc = ('android:id/button1')
    pwlogin_botton_loc = ("com.meipingmi.manager:id/tv_pwd_login")
    et_phone_loc = ("com.meipingmi.manager:id/et_phone")
    et_pwd_loc = ("com.meipingmi.manager:id/et_pwd")
    login_botto_loc = ('com.meipingmi.manager:id/btn_login')
    msg_loc =('com.meipingmi.manager:id/msg_notify')


    def setting_botton_link(self):
        self.find_element(self.setting_botton_loc).click()
        time.sleep(2)           #点击系统设置


    def run_case(self,value):
        self.find_element(self.about_loc).click()
        time.sleep(2)          #点击关于
        self.find_element(self.checkversion_botto_loc).click()
        time.sleep(2)  # 点击版本更新
        self.find_element(self.back_botto_loc).click()
        time.sleep(2)  # 点击返回按钮
        self.find_element(self.msg_loc).click()
        time.sleep(2)  # 点击消息通知
        self.find_element(self.back_botto_loc).click()
        time.sleep(2)  # 点击返回按钮

    def run_updatapwd(self,value):
        self.find_element(self.update_pwd_loc).click()
        time.sleep(2)  # 点击修改密码
        self.find_element(self.old_pwd_loc).send_keys(value)
        time.sleep(2)  # 输入旧密码

    def run_newpwd(self,value):
        self.find_element(self.new_pwd_loc).send_keys(value)
        time.sleep(2)  # 输入新密码

    def run_confirm_newpwd(self,value):
        self.find_element(self.new_pwd_confirm_loc).send_keys(value)
        time.sleep(2)  # 输入确认密码
        self.find_element(self.confirm_botton_loc).click()
        time.sleep(2)  # 点击确认按钮

     #退出登录
  #  def run_exit(self,value):
  #      self.find_element(self.exit_botton_loc).click()
  #      time.sleep(2)  # 点击退出登录按钮
  #       self.find_element(self.exit_no_botton_loc).click()
  #      time.sleep(2)  # 选择否
  #      self.find_element(self.exit_botton_loc).click()
  #      time.sleep(2)  # 点击退出登录按钮
  #      self.find_element(self.exit_yes_botton_loc).click()
  #     time.sleep(2)  # 点击是


    #退出登录返回登录页面，使用新密码登录
    def login_button_link(self):
        self.find_element(self.pwlogin_botton_loc).click()
        time.sleep(5)           #点击密码登录

    def run_case1(self,value):
        self.find_element(self.et_phone_loc).send_keys(value)
        time.sleep(5)          #输入手机号码

    def run_case2(self, value):
        self.find_element(self.et_pwd_loc).send_keys(value)
        time.sleep(5)    #输入密码
        self.find_element(self. login_botto_loc).click()
        time.sleep(5)    #点击登录按钮
