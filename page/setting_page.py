import time

import allure

from base.base_action import BaseAction
import page
class SettingPage(BaseAction):
    def __init__(self,driver):
        BaseAction.__init__(self,driver)

    # 退出用户
    @allure.step("设置页面 退出账号")
    def login_out_account(self):
        time.sleep(1)
        # 1.向上滑动页面
        allure.attach("退出","向上滑动")
        self.swipe_screen(1)
        # 2.点击退出
        allure.attach("退出", "点击退出按钮")
        self.click_element(page.setting_center_login_out_btn)
        # 3.点击弹出框的确认
        allure.attach("退出", "点击确认按钮")
        self.click_element(page.setting_center_login_dialog_confirm_btn)
