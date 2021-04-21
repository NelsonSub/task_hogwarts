# -*- coding:UTF-8 -*-
import time

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from fourth_work.page.add_department import AdddepartmentPage
from fourth_work.page.base import Base
# class Contacts:
#     def __init__(self):
#         self.driver = webdriver.Chrome()
#
#     def get_contacts(self):
#
#         self.driver.get('https://work.weixin.qq.com/wework_admin/frame#apps')
#         with open("cookie_data.yaml", encoding="UTF-8") as f:
#             yaml_data = yaml.safe_load(f)
#         for cookie in yaml_data:
#             self.driver.add_cookie(cookie)
#         with open("data1.yaml", "w", encoding="UTF-8") as f:
#             yaml.dump(self.driver.get_cookies(), f)
#
#         self.driver.get('https://work.weixin.qq.com/wework_admin/frame#contacts')
#
#     def contacts_add(self):
#
#         sleep(1)
#         self.driver.find_element(By.CSS_SELECTOR, 'div.ww_operationBar a.js_add_member').click()
#         return ContactsAdd(self.driver)
#     def get_contacts_list(self):
#         names = self.driver.find_elements(By.CSS_SELECTOR,'#member_list  td:nth-child(2)')
#
#         return names



class ContactsPage(Base):
    __ele_create_party = (By.CSS_SELECTOR,'ul > li:nth-child(1) > a.js_create_party')
    __ele_create_dropdown = (By.CSS_SELECTOR,'a.member_colLeft_top_addBtnWrap.js_create_dropdown')
    __ele_jstree_anchor = (By.CSS_SELECTOR,'a.jstree-anchor')
    def goto_add_department(self):

        self.find(self.__ele_create_dropdown).click()
        self.find(self.__ele_create_party).click()
        # #点击+
        # self.driver.find_element(By.CSS_SELECTOR,'a.member_colLeft_top_addBtnWrap.js_create_dropdown').click()
        # #点击添加部门
        # self.driver.find_element(By.CSS_SELECTOR,'ul > li:nth-child(1) > a.js_create_party').click()
        return AdddepartmentPage(self.driver)

    def get_department_list(self):
        #获取部门列表
        time.sleep(1)
        elements = self.finds(self.__ele_jstree_anchor)
        # elements = self.driver.find_elements(By.CSS_SELECTOR,'a.jstree-anchor')
        department_list = []
        for ele in elements:
            department_list.append(ele.text)

        print(department_list)

        return department_list