# -*- coding:UTF-8 -*-

import pytest
import allure


@allure.feature('计算器')
class Testcalculator:


    @pytest.mark.run(order = 2)
    @allure.story('加法')
    def test_add(self,Calculator_init,get_add_datas,case_init):
        result = Calculator_init.add(get_add_datas[0],get_add_datas[1])
        print('\n预期计算结果为：{}'.format(get_add_datas[2]))
        print('实际计算结果为：{}'.format(result))
        if isinstance(result,float):
            assert get_add_datas[2] == round(result,2)
        else:
            assert get_add_datas[2] == result

    @allure.story('除法')
    @pytest.mark.run(order = 1)
    def test_div(self,Calculator_init,get_div_datas,case_init):
        try:
            result = Calculator_init.div(get_div_datas[0],get_div_datas[1])
            if isinstance(result,float):
                result = round(result,2)
            print('\n预期计算结果为：{}'.format(get_div_datas[2]))
            print('实际计算结果为：{}'.format(result))
            assert get_div_datas[2] == result
        except ZeroDivisionError:
            print('除数不能为零')




