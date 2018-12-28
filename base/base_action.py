import os

import allure
import yaml
from appium.webdriver.common.touch_action import TouchAction
import time

from selenium.webdriver.common.by import By


class BaseAction:
    def __init__(self,driver):
        self.driver=driver

    def click_element(self,loc):
        self.find_element(loc).click()

    def long_press_element(self,loc):
        el =self.find_element(loc)
        TouchAction(self.driver).long_press(el).perform()

    def input_element(self,loc,content):
        self.find_element(loc).clear()
        self.find_element(loc).send_keys(content)

    def find_element(self,loc):
        time.sleep(1)
        # self.driver.implicitly_wait(10)
        return self.driver.find_element(loc[0],loc[1])

    def find_elements(self,loc):
        self.driver.implicitly_wait(10)
        return self.driver.find_elements(loc[0], loc[1])

    # 滑动
    def swipe_screen(self,tag):
        time.sleep(1)
        screen_size =self.driver.get_window_size()
        width=screen_size.get("width") # 宽度
        height=screen_size.get("height") # 高度
        if tag == 1: # 向上滑动
            self.driver.swipe(width * 0.5,height * 0.8,width * 0.5,height * 0.3)
        if tag == 2: # 向下滑动
            self.driver.swipe(width * 0.5, height * 0.3, width * 0.5, height * 0.8)
        if tag == 3: # 向左滑动
            self.driver.swipe(width * 0.8, height * 0.5, width * 0.3, height * 0.5)
        if tag == 4: # 向右滑动
            self.driver.swipe(width * 0.3, height * 0.5, width * 0.8, height * 0.5)

    # 截图
    @allure.step("截图")
    def get_screen(self):
        path="./screen/{}.png".format(int(time.time()))
        self.driver.get_screenshot_as_file(path)

    # 获取toast
    @allure.step("获取toast信息")
    def get_toast(self,mesge):
        path ="//*[contains(@text,'{}')]".format(mesge)
        toast_el=(By.XPATH,path)
        return self.find_element(toast_el).text





