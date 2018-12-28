import os,sys
sys.path.append(os.getcwd())
import time
import allure
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
        get_msg=s.get("get_msg")
        expect_msg=s.get("expect_msg")
        data_yaml.append((username, password,tag,get_msg,expect_msg))
    return data_yaml


class TestLogin:
    def setup_class(self):
        self.driver=BaseDriver().init_driver("com.yunmall.lc","com.yunmall.ymctoc.ui.activity.MainActivity")
        self.navigation=NavigationPage(self.driver)

    def teardown_class(self):
        self.driver.quit()
    @allure.step("登录开始")
    @pytest.mark.parametrize("username,password,tag,get_msg,expect_msg",read())
    def testlogin(self,username,password,tag,get_msg,expect_msg):
        # 1. 点击 home页面的 我
        self.navigation.get_home_page().click_me()
        # 2.点击 注册页面的 已有账号,去登录
        self.navigation.get_sign_in_page().click_sign_in_exit_account_login()
        # 3.填写 登录页面的 账号 密码 点击登录
        print()
        print(username, password, tag)
        time.sleep(1)
        self.navigation.get_login_in_page().login_in(username,password)
        # 4.判断是否登录成功
        if tag==1:
            try:
                login_stat=self.navigation.get_person_center_page().is_login_sucess()
                self.navigation.get_person_center_page().click_person_center_setting()
                self.navigation.get_setting_page().login_out_account()
                # 断言失败 截图提示
                assert login_stat,self.navigation.get_login_in_page().get_screen()
            except:
                # 若有错误 截图
                self.navigation.get_login_in_page().get_screen()
                # 关闭登录页面
                self.navigation.get_login_in_page().close_login_in()
        else:
            try:
                toast_data=self.navigation.get_login_in_page().get_toast(get_msg)
                assert toast_data==expect_msg,self.navigation.get_login_in_page().get_screen()
            finally:
                # 最后都要关闭登录页面
                self.navigation.get_login_in_page().close_login_in()


