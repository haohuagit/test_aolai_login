# from appium.webdriver import webdriver
from appium import webdriver


class BaseDriver:
    def init_driver(self,app_package,app_activity):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = '192.168.132.101:5555'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        desired_caps['appPackage'] = app_package
        desired_caps['appActivity'] = app_activity
        desired_caps['automationName'] = 'Uiautomator2'
        return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
