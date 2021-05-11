# -*- coding:UTF-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from sixth.page.base_page import Base_Page
from sixth.page.member_info_edit_page import MemberInfoEdit_Page


class MemberInfoSet_Page(Base_Page):

    def goto_member_info_edit(self):
        self.find(MobileBy.XPATH,"//*[@text='编辑成员']").click()
        return MemberInfoEdit_Page(self.driver)
