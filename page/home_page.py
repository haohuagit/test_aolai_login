import allure

from base.base_action import BaseAction
import page

"""
home页 首页 分类 购物车 我
"""
class HomePage(BaseAction):
    def __int__(self,driver):
        BaseAction.__init__(self,driver)

    # 点击 我
    @allure.step("在home页面 点击我")
    def click_me(self):
        self.click_element(page.home_me_tab)
