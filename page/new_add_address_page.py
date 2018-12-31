import time
from selenium.webdriver.common.by import By

from base.base_action import BaseAction
import page,allure

class NewAddAddressPage(BaseAction):
    def __init__(self,driver):
        BaseAction.__init__(self,driver)

    # 点击选择地区
    def click_adress(self,address):
        path="//*[contains(@text,'{}')]".format(address)
        address_el=(By.XPATH,path)
        while True:
            try:
                self.find_element(address_el)
                return self.click_element(address_el)
            except:
                self.swipe_screen(1)



    @allure.step("新增地址 新增信息")
    def new_address_add_news(self,receipt,phone,province,detail):
        allure.attach("新增信息","收件人")
        time.sleep(1)
        self.input_element(page.new_adress_receipt_name,receipt)

        if phone != None:
            allure.attach("新增信息", "手机号")
            time.sleep(1)
            self.input_element(page.new_adress_phone,phone)

        if province != None:
            time.sleep(1)
            allure.attach("新增信息", "所属地区")
            self.click_element(page.new_adress_province)
            for i in province:

                self.click_adress(i)

        if detail != None:
            allure.attach("新增信息", "详细信息")
            time.sleep(1)
            self.input_element(page.new_adress_detail_address,detail)

        time.sleep(1)
        allure.attach("新增信息", "点击保存")
        self.click_element(page.new_adress_save)

    @allure.step("新增地址 关闭新增页面")
    def new_address_click_back(self):
        self.click_element(page.new_adress_back)


