# -*- coding:UTF-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from sixth.page.add_member_page import AddMember_Page
from sixth.page.base_page import Base_Page
from sixth.page.member_info_page import MemberInfo_Page


class Contact_Page(Base_Page):

    def goto_add_member(self):
        self.swipe_find('添加成员').click()
        return AddMember_Page(self.driver)

    def goto_member_info(self, name):
        self.swipe_find(name).click()
        return MemberInfo_Page(self.driver)

    def get_member_list(self):
        ele_member_list = self.driver.find_elements(MobileBy.XPATH,
                                                    "(//*[@class='android.widget.ListView']//*[@class = 'android.widget.TextView'])[position()<last()-1][position()>3]")
        name_list = []
        for el in ele_member_list:
            name_list.append(el.text)
            print(name_list)
        return name_list
