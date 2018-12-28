from page.home_page import HomePage
from page.login_in_page import LoginInPage
from page.person_center_page import PersonCenterPage
from page.setting_page import SettingPage
from page.sign_in_page import SignInPage

class NavigationPage:
    def __init__(self,driver):
        self.driver=driver

    # 获得home_page的实例对象
    def get_home_page(self):
        return HomePage(self.driver)

    # 获得login_in_page的实例对象
    def get_login_in_page(self):
        return LoginInPage(self.driver)

    # 获得person_center_page的实例对象
    def get_person_center_page(self):
        return PersonCenterPage(self.driver)

    # 获得setting_page的实例对象
    def get_setting_page(self):
        return SettingPage(self.driver)

    # 获得sign_in_page的实例对象
    def get_sign_in_page(self):
        return SignInPage(self.driver)


