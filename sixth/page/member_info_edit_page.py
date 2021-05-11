# -*- coding:UTF-8 -*-
from time import sleep

from sixth.page.base_page import Base_Page
from appium.webdriver.common.mobileby import MobileBy


class MemberInfoEdit_Page(Base_Page):
    def del_member(self):
        self.swipe_find('删除成员').click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='确定']").click()
        from sixth.page.contact_page import Contact_Page
        return Contact_Page(self.driver)
