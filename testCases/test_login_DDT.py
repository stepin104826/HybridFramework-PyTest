from time import sleep

import pytest
from selenium import webdriver

from pageObjects.LoginPage import LoginPage

from utilities.readProperties import ReadConfig

from utilities.customLogger import LogGeneration

from utilities import ExcelUtils

class Test_002_DDT_login:

    baseURL = ReadConfig.getApplicationURL()
    path = ".//testData/LoginTestdata.xlsx"
    logger = LogGeneration.logGen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):

        self.logger.info("****************** Test_002_DDT_Login ***********************")
        self.logger.info("************ Verifying Login DDT Test*************")
        self.driver = setup

        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5000)

        self.lpobject = LoginPage(self.driver)

        self.rows = ExcelUtils.getRowCount(self.path, "Sheet1")
        self.cols = ExcelUtils.getColCount(self.path,"Sheet1")
        print("Row Count in the excel file: ", self.rows)
        print("Column Count in the excel file: ", self.cols)

        for r in range(2, self.rows+1):
            self.email = ExcelUtils.readData(self.path, "Sheet1", r, 1)
            self.password = ExcelUtils.readData(self.path, "Sheet1", r, 2)

            self.lpobject.enterEmail(self.email)
            self.lpobject.enterPassword(self.password)
            self.lpobject.clickLogin()
            sleep(3)

            actual_title = self.driver.title
            expected_title = "Dashboard / nopCommerce administration"

            self.logger.info(f"**************** Test data: {self.email}, {self.password}******************")
            if actual_title == expected_title:
                self.logger.info("******************** Test case passed ********************")
                self.lpobject.clickLogout()

            elif actual_title != expected_title:
                self.logger.info("******************** Test case failed ********************")

        self.driver.close()
        self.logger.info("**************** End of Login DDT TEST ****************")
        self.logger.info("**************** Test_002_DDT_Login ****************")





