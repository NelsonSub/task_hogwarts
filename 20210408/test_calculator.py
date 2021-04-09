# -*- coding:UTF-8 -*-

import pytest
import yaml
from Calculator import Calculator


class Testcalculator:

    def setup_class(self):
        print('\n开始执行测试用例')
        self.cal= Calculator()

    def teardown_class(self):
        print('所有测试用例已执行完毕')

    def setup(self):
        print('\n开始计算...')

    def teardown(self):
        print('结束计算！！！')

    @pytest.mark.parametrize('a,b,expect',yaml.safe_load(open('./test_add.yaml')))
    def test_add(self,a,b,expect):
        result = self.cal.add(a,b)
        print('\n预期计算结果为：{}'.format(expect))
        print('实际计算结果为：{}'.format(result))
        assert expect == result

    @pytest.mark.parametrize('a,b,expect',yaml.safe_load(open('./test_div.yaml')))
    def test_div(self,a,b,expect):

        result = self.cal.div(a,b)
        if not isinstance(result,str):
            result = round(result,2)
            expect = round(result,2)

        print('\n预期计算结果为：{}'.format(expect))
        print('实际计算结果为：{}'.format(result))
        assert expect == result




