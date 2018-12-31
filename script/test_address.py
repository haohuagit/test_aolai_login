import os,sys

import allure
import pytest

sys.path.append(os.getcwd())

from base.base_driver import BaseDriver
import page
from page.navigation_page import NavigationPage
from base.read_yaml import read_yaml

def read():
    datas=read_yaml("address_yaml.yaml")
    data_list=[]
    for s in datas.keys():
        tag=datas[s].get("tag")
        receipt=datas[s].get("receipt")
        phone=datas[s].get("phone")
        province=datas[s].get("province")

        detail=datas[s].get("detail")
        get_data=datas[s].get("get_data")
        expect=datas[s].get("expect")
        data_list.append((tag,receipt,phone,province,detail,get_data,expect))
    return data_list



class TestAddress:
    def setup_class(self):
        self.driver=BaseDriver().init_driver("com.yunmall.lc","com.yunmall.ymctoc.ui.activity.MainActivity")
        self.navigation_page=NavigationPage(self.driver)
        self.navigation_page.get_home_page().click_me()
        self.navigation_page.get_sign_in_page().click_sign_in_exit_account_login()
        self.navigation_page.get_login_in_page().login_in("13488834010", "159357li")
        self.navigation_page.get_person_center_page().click_person_center_setting()
        self.navigation_page.get_setting_page().click_adress_manage()

    def teardown_class(self):
        self.driver.quit()


    @allure.step("地址管理")
    @pytest.mark.parametrize("tag,receipt,phone,province,detail,get_data,expect",read())
    def test_address(self,tag,receipt,phone,province,detail,get_data,expect):
        print()
        print(tag,receipt,phone,province,detail,get_data,expect)
        self.navigation_page.get_address_manage_page().click_new_add_address()
        self.navigation_page.get_new_add_address_page().new_address_add_news(receipt,phone,province,detail)
        if tag==1:
            save_stat=self.navigation_page.get_address_manage_page().address_manage_is_save_success()
            assert save_stat,self.navigation_page.get_setting_page().get_screen()
            self.navigation_page.get_address_manage_page().del_address()

        else:
            try:
                result=self.navigation_page.get_setting_page().get_toast(get_data)
                assert result==expect,self.navigation_page.get_setting_page().get_screen()
            finally:
                self.navigation_page.get_new_add_address_page().new_address_click_back()










        # self.navigation_page.get_address_manage_page().del_address()






