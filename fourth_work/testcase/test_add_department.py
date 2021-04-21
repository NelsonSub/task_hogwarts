import allure
import pytest

from fourth_work.page.main import MainPage

@allure.feature("企业微信")
class Testdepartment:
    def setup(self):
        self.main = MainPage()

    def teardown(self):
        self.main.quit()
    @allure.story('添加部门')
    @pytest.mark.parametrize('department_name', ['市场部'])
    def test_add_department(self, department_name):
        # print(department_name)
        # print(self.main.goto_contacts().goto_add_department().adddepartment(department_name). \
        #       get_department_list())
        assert department_name in self.main.goto_contacts().goto_add_department().adddepartment(department_name). \
            get_department_list()
