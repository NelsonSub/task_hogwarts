# -*- coding:UTF-8 -*-
from page import contacts
from utils import get_cookie
from selenium.webdriver.common.by import By
from selenium import webdriver
import yaml
from time import sleep
class TestWork:

    def get_cookie(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address='127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=opt)

        self.driver.implicitly_wait(5)
        cookie = self.driver.get_cookies()

        with open("data.yaml", "w", encoding="UTF-8") as f:
            yaml.dump(cookie, f)


    def get_contacts(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#apps')
        with open("data.yaml", encoding="UTF-8") as f:
            yaml_data = yaml.safe_load(f)
        for cookie in yaml_data:
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#contacts')


    def add_contacts(self):
        #查找添加成员按钮
        self.driver.find_element(By.CSS_SELECTOR,'div.ww_operationBar a.js_add_member').click()
        sleep(5)
        self.driver.find_element(By.CSS_SELECTOR,'#username').send_keys('企业微信')
        self.driver.find_element(By.CSS_SELECTOR, '#memberAdd_acctid').send_keys('wechattest')
        self.driver.find_element(By.CSS_SELECTOR,'.ww_telInput_mainNumber').send_keys('12322222222')
        self.driver.find_element(By.CSS_SELECTOR,'a.qui_btn.ww_btn.js_btn_save').click()

        sleep(5)

    def test_add(self):

        self.get_cookie()
        self.get_contacts()



    def test_addContacts(self):

        get_cookie.get_cookie()
        cont = contacts.Contacts()
        cont.get_contacts()
        add = cont.contacts_add()
        contactdata = {'#username':'企业微信','#memberAdd_acctid':'wechattest','.ww_telInput_mainNumber':'12322222222'}

        add.contactsinput(contactdata)
        add.contactssave()
        print(cont.get_contacts_list())



