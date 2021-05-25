# -*- coding:UTF-8 -*-
import json


import allure

from tenth_work.api.contact.user import User
from tenth_work.common.fakedata import FakerData


@allure.feature('通讯录成员管理测试')
class TestUser:

    def setup_class(self):
        self.fake_data = FakerData()
        self.user = User()
        self.user.get_token('user')

    @allure.story("通讯录添加成员测试")
    @allure.title("通讯录添加成员测试")
    def test_user_create(self):
        name = self.fake_data.get_name()
        userid = 'testLI'
        department = [1]
        mobile = self.fake_data.get_phonenum()
        with allure.step("添加新用户"):
            result = self.user.create(userid, name, department, mobile)
            allure.attach(json.dumps(result,indent=2,ensure_ascii=False), attachment_type=allure.attachment_type.TEXT)
            assert result.get('status_code') == 200
            assert result.get('data').get('errcode') == 0
        with allure.step("查询已添加的用户进行断言"):
            get_result = self.user.get(userid)
            allure.attach(json.dumps(get_result, indent=2, ensure_ascii=False), attachment_type=allure.attachment_type.TEXT)
            assert get_result.get('status_code') == 200
            assert get_result.get('data').get('errcode') == 0
            assert get_result.get('data').get('mobile') == mobile
        # 删除已添加的成员
        with allure.step("删除已添加的用户清理数据"):
            self.user.delete(userid)
