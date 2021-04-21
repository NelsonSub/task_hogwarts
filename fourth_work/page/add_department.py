from selenium.webdriver.common.by import By

from fourth_work.page.base import Base


class AdddepartmentPage(Base):

    __ele_depart_name = (By.CSS_SELECTOR,'.qui_dialog_body .qui_inputText')
    __ele_party_list = (By.CSS_SELECTOR,'a.js_toggle_party_list')
    __ele_jstree_anchor = (By.CSS_SELECTOR,'.js_party_list_container .jstree-anchor')
    __ele_submit = (By.CSS_SELECTOR,'.ww_dialog_WithInput a.qui_btn.ww_btn.ww_btn_Blue')

    def adddepartment(self,departmenr_name):
        #输入添加部门名称
        self.find(self.__ele_depart_name).send_keys(departmenr_name)
        self.find(self.__ele_party_list).click()
        self.find(self.__ele_jstree_anchor).click()
        self.find(self.__ele_submit).click()
        # self.driver.find_element(By.CSS_SELECTOR,'.qui_dialog_body .qui_inputText').send_keys(departmenr_name)
        # #选择所属部门
        # self.driver.find_element(By.CSS_SELECTOR,'a.js_toggle_party_list').click()
        # self.driver.find_element(By.CSS_SELECTOR,'.js_party_list_container .jstree-anchor').click()
        # #点击确定
        # self.driver.find_element(By.CSS_SELECTOR,'.ww_dialog_WithInput a.qui_btn.ww_btn.ww_btn_Blue').click()

        from fourth_work.page.contacts import ContactsPage
        return ContactsPage(self.driver)
        pass