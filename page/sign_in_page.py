import allure

from base.base_action import BaseAction
import page
"""
注册页面
"""
class SignInPage(BaseAction):
    def __init__(self,driver):
        BaseAction.__init__(self,driver)

    # 点击 已有账号,去登录
    @allure.step("注册页面 点击已有账号,去登录")
    def click_sign_in_exit_account_login(self):
        self.click_element(page.sign_in_exit_account_login)