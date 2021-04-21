# -*- coding:UTF-8 -*-

from selenium import webdriver
import yaml
import os


class Base:

    def __init__(self, base_driver: webdriver = None):
        """
        driver 重复实例化会 导致页面启动多次
        解决driver 重复实例化的问题
        :param drvier:
        """

        if base_driver is None:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(5)
            self.driver.maximize_window()
            self.driver.get('https://work.weixin.qq.com/wework_admin/frame#apps')
            # path = os.path.dirname(os.getcwd())
            # datapath =os.path.join(path,'data/cookie_data.yaml')
            with open("../data/cookie_data.yaml", encoding="UTF-8") as f:
                yaml_data = yaml.safe_load(f)
            for cookie in yaml_data:
                self.driver.add_cookie(cookie)
            self.driver.get('https://work.weixin.qq.com/wework_admin/frame#contacts')


        else:
            self.driver = base_driver

    def find(self, by, ele=None):
        '''

        :param by: 定位方式
        :param ele: 元素定位信息
        :return:
        '''
        if ele is None:
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by,ele)
    def finds(self, by, ele=None):
        '''

        :param by: 定位方式
        :param ele: 元素定位信息
        :return:
        '''
        if ele is None:
            return self.driver.find_elements(*by)
        else:
            return self.driver.find_elements(by,ele)

