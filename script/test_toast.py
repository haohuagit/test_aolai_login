import os,sys

import time

sys.path.append(os.getcwd())
import pytest
from base.base_driver import BaseDriver
from page.navigation_page import NavigationPage
from base.read_yaml import read_yaml
import page
# 读取数据
def read():
    datas =read_yaml("data_yaml.yaml")
    data_yaml = []
    for i in datas.keys():
        s=datas.get(i)
        username = s.get("username")
        password = s.get("password")
        tag=s.get("tag")
        data_yaml.append((username, password,tag))
    return data_yaml

class TestLogin:
    def setup_class(self):
        self.driver=BaseDriver().init_driver("com.yunmall.lc","com.yunmall.ymctoc.ui.activity.MainActivity")
        self.navigation=NavigationPage(self.driver)

    def teardown_class(self):
        self.driver.quit()


    def testlogin(self):
        # 1. 点击 home页面的 我
        self.navigation.get_home_page().click_me()
        # 2.点击 注册页面的 已有账号,去登录
        self.navigation.get_sign_in_page().click_sign_in_exit_account_login()
        # 3.填写 登录页面的 账号 密码 点击登录
        # print()
        # print(username, password, tag)
        self.navigation.get_login_in_page().login_in("123","11")
        # 4.获取toast
        time.sleep(1)
        el =self.navigation.get_sign_in_page().find_element(page.sign_in_toast)
        print(el.text)


