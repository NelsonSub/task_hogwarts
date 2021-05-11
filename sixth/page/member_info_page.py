# -*- coding:UTF-8 -*-
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from sixth.page.base_page import Base_Page
from sixth.page.member_info_set_page import MemberInfoSet_Page


class MemberInfo_Page(Base_Page):

    def goto_memberinfoset(self):
        sleep(6)
        self.find(MobileBy.XPATH,"//*[@text='个人信息']/../../../../.././/*[android.widget.RelativeLayout]").click()
        return MemberInfoSet_Page(self.driver)
