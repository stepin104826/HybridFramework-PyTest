from time import sleep

import pytest
from selenium import webdriver

from pageObjects.LoginPage import LoginPage

from utilities.readProperties import ReadConfig

from utilities.customLogger import LogGeneration

class Test_001_login:

    baseURL = ReadConfig.getApplicationURL()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()

    logger = LogGeneration.logGen()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):

        self.logger.info("***************** Test_001_Login ***********************")
        self.logger.info("************ Verifying Homepage Title *************")
        self.driver = setup

        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5000)
        sleep(3)

        page_title = self.driver.title

        if page_title == "Your store. Login":
            assert True
            self.logger.info("******************** Test case passed ********************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.info("******************** Test case failed ********************")
            assert False

    @pytest.mark.sanity
    def test_login(self, setup):

        self.logger.info("****************** Test_002_Login ***********************")
        self.logger.info("************ Verifying Login *************")
        self.driver = setup

        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5000)

        lpobject = LoginPage(self.driver)

        lpobject.enterEmail(self.email)
        lpobject.enterPassword(self.password)
        sleep(3)
        lpobject.clickLogin()
        sleep(3)

        page_title = self.driver.title

        if page_title == "Dashboard / nopCommerce administration":
            self.logger.info("******************** Test case passed ********************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            lpobject.clickLogout()
            self.driver.close()
            self.logger.info("******************** Test case failed ********************")
            assert False






