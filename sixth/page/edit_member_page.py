# -*- coding:UTF-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from sixth.page.base_page import Base_Page


class EditMember_Page(Base_Page):
    def edit_member(self,name,mobile):

        self.find(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
        self.find(MobileBy.XPATH, "//*[contains(@text,'手机')]/..//android.widget.EditText").send_keys(mobile)
        self.find(MobileBy.XPATH, '//*[contains(@text,"发送邀请通知")]').click()
        self.find(MobileBy.XPATH, '//*[contains(@text,"保存")]').click()
        # self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
        # self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'手机')]/..//android.widget.EditText").send_keys(mobile)
        # self.driver.find_element(MobileBy.ID, '//*[contains(@text,"发送邀请通知")]').click()
        # self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"保存")]').click()
        from fifth.page.addmemberpage import AddMemberPage
        return AddMemberPage(self.driver)


