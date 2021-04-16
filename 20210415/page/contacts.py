# -*- coding:UTF-8 -*-
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from page.contacts_add import ContactsAdd
from time import sleep

class Contacts:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_contacts(self):

        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#apps')
        with open("data.yaml", encoding="UTF-8") as f:
            yaml_data = yaml.safe_load(f)
        for cookie in yaml_data:
            self.driver.add_cookie(cookie)
        with open("data1.yaml", "w", encoding="UTF-8") as f:
            yaml.dump(self.driver.get_cookies(), f)

        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#contacts')

    def contacts_add(self):

        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, 'div.ww_operationBar a.js_add_member').click()
        return ContactsAdd(self.driver)
    def get_contacts_list(self):
        names = self.driver.find_elements(By.CSS_SELECTOR,'#member_list  td:nth-child(2)')

        return names
