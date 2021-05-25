# -*- coding:UTF-8 -*-

from faker import Faker


class FakerData:
    def __init__(self):
        self.faker = Faker('zh-CN')

    def get_name(self):
        name = self.faker.name()
        return "test" + name

    def get_phonenum(self):
        phonenum = self.faker.phone_number()

        return phonenum

