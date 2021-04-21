from selenium.webdriver.common.by import By

from fourth_work.page.base import Base
from  fourth_work.page.contacts import ContactsPage


class MainPage(Base):
    __ele_menu_contacts = (By.CSS_SELECTOR, '#menu_contacts')
    def goto_contacts(self):
        # self.driver.find_element(By.CSS_SELECTOR, '#menu_contacts').click()
        self.find(self.__ele_menu_contacts).click()
        return ContactsPage(self.driver)

    def quit(self):
        self.driver.quit()
