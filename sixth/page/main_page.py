# -*- coding:UTF-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from sixth.page.base_page import Base_Page
from sixth.page.contact_page import Contact_Page


class Main_Page(Base_Page):

    def goto_contact(self):
        # 点击通讯录
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        return Contact_Page(self.driver)