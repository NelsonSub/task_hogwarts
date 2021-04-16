# -*- coding:UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class ContactsAdd:
    def __init__(self, driver: webdriver):
        self.driver = driver

    def contactsinput(self,contactdata ):
        # self.driver.find_element(By.CSS_SELECTOR,'div.ww_operationBar a.js_add_member').click()
        for key, value in contactdata.items():
            self.driver.find_element(By.CSS_SELECTOR, key).send_keys(value)
        # self.driver.find_element(By.CSS_SELECTOR, '#username').send_keys('企业微信')
        # self.driver.find_element(By.CSS_SELECTOR, '#memberAdd_acctid').send_keys('wechattest')
        # self.driver.find_element(By.CSS_SELECTOR,'.ww_telInput_mainNumber').send_keys('12322222222')

    def contactssave(self):
        self.driver.find_element(By.CSS_SELECTOR, 'a.qui_btn.ww_btn.js_btn_save').click()
        sleep(10)



