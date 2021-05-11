# -*- coding:UTF-8 -*-
from appium import webdriver
from sixth.page.base_page import Base_Page
from sixth.page.main_page import Main_Page


class App(Base_Page):

    def start(self):
        # 如果没有driver则初始化
        if self.driver is None:
            # 启动APP
            caps = {
                "platformName": "android",
                "deviceName": "test",
                "appPackage": "com.tencent.wework",
                "appActivity": ".launch.WwMainActivity",
                "autoGrantPermissions": "true",
                "noReset": "true"
            }
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
            self.driver.implicitly_wait(5)
            self.driver.update_settings({'waitForIdleTimeout': 0})

        else:
            # 如果有driver 则复用driver，启动app即可
            self.driver.launch_app()
        return self

    def stop(self):
        # app退回后台运行
        self.driver.close_app()

    def restart(self):
        self.driver.close_app()
        # 启动APP
        self.driver.launch_app()

    def quit(self):
        # 销毁资源
        self.driver.quit()

    def goto_main(self):
        return Main_Page(self.driver)


