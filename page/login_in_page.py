import time

import allure

from base.base_action import BaseAction
import page
"""
登录页面
"""

class LoginInPage(BaseAction):
    def __init__(self,driver):
        BaseAction.__init__(self,driver)


    #  登录信息
    @allure.step("登录页面")
    def login_in(self,name,password):
        # 1.登录手机号
        allure.attach("登录","输入用户名")
        self.input_element(page.login_username_id,name)
        # 2.密码
        allure.attach("登录", "输入密码")
        self.input_element(page.login_password_id,password)
        # 3.点击登录
        allure.attach("登录", "点击登录按钮")
        self.click_element(page.login_login_in_btn)


    # 信息填错时,退出
    @allure.step("注册页面 关闭登录")
    def close_login_in(self):
        time.sleep(1)
        self.click_element(page.login_login_out_btn)
