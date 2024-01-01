import time

import pytest
from selenium import webdriver
from PageObject.LoginPage import LoginPage
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()

    logger= LogGen.loggen()

    def test_homePageTitle(self,setup):

        self.logger.info("***********************Test_001_Login**************************")
        self.logger.info("***********************Test_001_Login**************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        print(act_title)
        time.sleep(3)
        self.driver.save_screenshot(r"E:\AUtomation_projects\Screenshots\test_login_failure.png")

        if act_title=="Your store. Login":

            assert True
            self.logger.info("***********************Home Page Title Test Pass**************************")

        else:
            self.driver.save_screenshot(r"E:\AUtomation_projects\Screenshots" + "header.png")
            self.driver.close()
            self.logger.warning("***********************Home Page Title Test Fail**************************")
            assert False


    def test_login(self,setup):
        self.logger.info("***********************Login Test Start**************************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            self.driver.close()
            assert True
            self.logger.info("***********************Login Test Pass**************************")


        else:
            self.driver.save_screenshot(r"E:\AUtomation_projects\Screenshots\\test_login.png")
            self.driver.close()
            self.logger.error("***********************Login Test Fail**************************")
            assert False