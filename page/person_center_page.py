import allure

from base.base_action import BaseAction
import page
"""
个人中心
"""
class PersonCenterPage(BaseAction):
    def __init__(self,driver):
        BaseAction.__init__(self,driver)

    # 点击设置按钮
    @allure.step("个人中心页面 点击设置按钮")
    def click_person_center_setting(self):
        self.click_element(page.person_center_setting_btn)

    # 是否登录成功 查看全部订单
    @allure.step("判断是否登录成功")
    def is_login_sucess(self):
        try:
            allure.attach("个人中心","定位到全部订单,登录成功")
            self.find_element(page.person_center_all_order)
            return True
        except:
            allure.attach("个人中心", "没有定位到全部订单,登录失败")
            return False



