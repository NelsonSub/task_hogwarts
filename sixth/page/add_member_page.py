# -*- coding:UTF-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from sixth.page.base_page import Base_Page
from sixth.page.edit_member_page import EditMember_Page


class AddMember_Page(Base_Page):

    def goto_edit_member(self):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        return EditMember_Page(self.driver)

    def find_toast(self):
        #断言toast
        self.find(MobileBy.XPATH, "//*[@text='添加成功']")