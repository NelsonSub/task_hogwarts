# -*- coding:UTF-8 -*-

# 计算器
class Calculator:
    # 相加
    def add(self, a, b):
        return a + b

    # 相除
    def div(self, a, b):
        if b != 0:
            return a / b
        else:
            return 'error'

