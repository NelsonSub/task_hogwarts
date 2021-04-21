# -*- coding:UTF-8 -*-

from fourth.page.contacts import ContactsPage
from fourth.page.add_member import Add_Member_Page


class MainPage:

    def goto_contacts(self):
        return ContactsPage()

    def goto_add_member(self):
        return Add_Member_Page()
