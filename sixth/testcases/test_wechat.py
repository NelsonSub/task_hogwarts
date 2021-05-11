# -*- coding:UTF-8 -*-
from sixth.page.app import App


class TestWechat:

    def setup_class(self):
        self.app = App()

    def setup(self):
        # 启动 app
        self.main = self.app.start().goto_main()
        self.name = '张三'
        self.mobile = '12321541245'

    def setdown(self):
        self.app.stop()

    def teardown_class(self):
        self.app.quit()

    def test_add_member(self):
        self.main.goto_contact().goto_add_member().goto_edit_member().edit_member(self.name, self.mobile).find_toast()

    def test_del_member(self):
        name_list = self.main.goto_contact().goto_member_info(self.name). \
            goto_memberinfoset().goto_member_info_edit(). \
            del_member().get_member_list()

        assert self.name not in name_list
