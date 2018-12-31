from base.base_action import BaseAction
import page,allure

class AddressManagePage(BaseAction):
    def __init__(self,driver):
        BaseAction.__init__(self,driver)

    @allure.step("地址管理 新增")
    def click_new_add_address(self):
        self.click_element(page.address_manage_new_add_address)

    @allure.step("地址管理 删除第一个地址")
    def del_address(self):
        self.click_element(page.address_manage_editor_save)
        self.click_element(page.address_manage_delete_address)
        self.click_element(page.del_address_accept)

    @allure.step("地址管理 判断是否保存成功")
    def address_manage_is_save_success(self):
        try:
            allure.attach("是否保存成功","定位到新增地址,成功")
            self.find_element(page.address_manage_new_add_address)
            return True
        except:
            allure.attach("是否保存成功", "没有定位到新增地址,失败")
            return False

    @allure.step("地址管理 修改地址")
    def address_manage_modify_news(self):
        self.click_element(page.address_manage_editor_save)
        self.click_element(page.address_manage_modify_address)
        self.input_element(page.new_adress_receipt_name)

