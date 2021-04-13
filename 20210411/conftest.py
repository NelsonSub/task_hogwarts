# -*- coding:UTF-8 -*-
from typing import List

import pytest
import yaml
from Calculator import Calculator
@pytest.fixture(scope='class')
def Calculator_init():
    print('\n测试用例开始执行')
    cal = Calculator()
    yield cal

    print('测试用例运行完毕')


def get_data(file):
    with open(file,encoding='utf-8') as f:
        data = yaml.safe_load(f)

    return data

@pytest.fixture(params=get_data('./test_add.yaml')['param'],ids=get_data('./test_add.yaml')['ids'])
def get_add_datas(request):
    return request.param

@pytest.fixture(params=get_data('./test_div.yaml')['param'],ids=get_data('./test_div.yaml')['ids'])
def get_div_datas(request):
    return request.param



# def test_get_data():
#     print(get_data('./test_div.yaml'))
@pytest.fixture()
def case_init():
    print('\n开始计算！！！')
    yield
    print('结束计算')

def pytest_collection_modifyitems(session, config, items: List):

    for item in items:
        print(dir(item))
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
# def pytest_addoption(parser,pluginmanager):
#     parser.addoption("--env",  ##注册一个命令行选项
#                      default="store",
#                      dest="env",
#                      help="set test run env")
