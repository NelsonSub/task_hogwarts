# -*- coding:UTF-8 -*-
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
import pytest


class Test_Wework:

    def setup(self):
        caps = {
            "platformName": "android",
            "deviceName": "test",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.WwMainActivity",
            "autoGrantPermissions": "true",
            "noReset": "true"
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        self.driver.implicitly_wait(5)
        self.driver.update_settings({'waitForIdleTimeout': 0})

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize('name, mobile', [('app', '13424163869')])
    def test_add_contacts(self, name, mobile):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="添加成员"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/ays').send_keys(name)
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/f4m').send_keys(mobile)
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/esx').click()
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/ac9').click()
        self.driver.back()
        self.driver.back()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="{}"]'.format(name)).click()
