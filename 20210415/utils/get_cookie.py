# -*- coding:UTF-8 -*-
import yaml
from selenium import webdriver


def get_cookie():
    opt = webdriver.ChromeOptions()
    opt.debugger_address = '127.0.0.1:9222'
    driver = webdriver.Chrome(options=opt)

    driver.implicitly_wait(5)
    cookie = driver.get_cookies()

    with open("data.yaml", "w", encoding="UTF-8") as f:
        yaml.dump(cookie, f)




