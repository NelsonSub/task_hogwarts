# -*- coding:UTF-8 -*-
import json
from datetime import datetime

import pytest
import allure
from eighth.api.add_corp_tag import add_corp_tag
from eighth.api.edit_corp_tag import edit_corp_tag
from eighth.api.get_corp_tag_list import get_corp_tag_list
from eighth.api.gettoken import get_token
from eighth.api.del_corp_tag import del_corp_tag
import jsonpath


@allure.feature("客户标签管理测试")
class TestCorp:
    token = None

    def setup_class(self):
        self.token = get_token().json().get('access_token')

    @allure.story("添加标签")
    @pytest.mark.parametrize('tag_name,group_name', [['ces', 'gg']])
    def test_add_corp(self, tag_name, group_name):
        result = add_corp_tag(self.token, tag_name, group_name).json()
        assert result['errcode'] == 0
        group_id = result.get('tag_group').get('group_id')
        search_result = get_corp_tag_list(self.token, group_id).json()
        assert search_result['errcode'] == 0
        tag_name_list = jsonpath.jsonpath(search_result, '$..name')
        tag_group_list = jsonpath.jsonpath(search_result, '$..group_name')

        assert tag_name in tag_name_list

        assert group_name in tag_group_list

    @allure.story("编辑标签组")
    # @pytest.mark.parametrize('new_name', ['group_new'])
    def test_edit_corp(self):
        new_name = 'name' + datetime.now().strftime('%Y%m%d%H%M%S%f')[:-3]
        search_result = get_corp_tag_list(self.token).json()
        assert search_result['errcode'] == 0
        group_id = jsonpath.jsonpath(search_result, '$..group_id')[0]

        edit_result = edit_corp_tag(self.token, group_id, new_name).json()
        assert edit_result['errcode'] == 0
        search_result = get_corp_tag_list(self.token).json()
        assert search_result['errcode'] == 0
        assert new_name in jsonpath.jsonpath(search_result, '$..group_name')

    @allure.story("删除标签")
    @pytest.mark.parametrize('tag_name', ['ces'])
    def test_del_corp(self, tag_name):
        search_result = get_corp_tag_list(self.token).json()
        assert search_result['errcode'] == 0
        tag_id = jsonpath.jsonpath(search_result, f'$.[?(@.name == "{tag_name}")].id')
        del_result = del_corp_tag(self.token, tag_id)
        assert jsonpath.jsonpath(del_result, f'$.[?(@.name == "{tag_name}")]') is False
