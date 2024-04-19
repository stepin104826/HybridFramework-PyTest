import string
import random
from time import sleep

import pytest
from selenium.webdriver.common.by import By

from utilities.customLogger import LogGeneration
from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomerPage

class Test_003_AddCustomer:
    pageURL = ReadConfig.getApplicationURL()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()

    logger = LogGeneration.logGen()

    @pytest.mark.smoke
    def test_addCustomer(self,setup):
        self.logger.info("********************* Test_003_AddCustomers ***************************")

        self.driver = setup
        self.driver.get(self.pageURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5000)

        self.logger.info("************ Verifying Login *************")
        plObject = LoginPage(self.driver)
        plObject.enterEmail(self.email)
        plObject.enterPassword(self.password)
        sleep(3)
        plObject.clickLogin()

        self.logger.info("************ Verifying Homepage Title *************")
        if self.driver.title == "Dashboard / nopCommerce administration":
            self.logger.info(f"************ Correct Homepage Title : {self.driver.title}*************")
            self.logger.info("************ Verifying Add Customer Option *************")
            acObject = AddCustomerPage(self.driver)
            acObject.clickCustomerMenu()
            acObject.chooseCustomerOption()
            acObject.clickAddNewButton()
            acObject.enterCustEmail(self.randomEmailGenerator() + "@gmail.com")
            acObject.enterCustPassword(self.randomPasswordGenerator())
            acObject.enterCustFirstName(self.randomFirstNameGenerator())
            acObject.enterCustLastName(self.randomLastNameGenerator())
            acObject.selectGender(random.choice(["Male","Female"]))
            acObject.selectDOB("8/17/1998")
            acObject.enterCompanyName(random.choice(["LTTS","Deloitte","Wipro","Amazon","Apple","Facebook"]))
            acObject.checktaxexempt(random.choice([True,False]))
            acObject.inputnewsletter(random.choice(["Your store name", "Test store 2"]))
            sleep(2)
            acObject.inputCustomerRoles()
            sleep(2)
            acObject.selectVendorManager()
            sleep(2)
            acObject.checkActive()
            acObject.enterAdminComment("These are the customer details")
            sleep(2)
            acObject.clickSave()
            sleep(2)
            alert = self.driver.find_element(By.XPATH,'//div[@class="alert alert-success alert-dismissable"]');
            alerttext = alert.text
            print(alerttext)
            if "The new customer has been added successfully." in alerttext:
                self.logger.info("************ Customer Added Successfully *************")
                self.driver.quit()
                self.logger.info("************ Test case Passed *************")

            else:
                self.logger.info("************ Customer Not Added Successfully *************")
                self.driver.quit()
                self.logger.info("************ Test case Failed *************")

        else:
            self.logger.info("************ Incorrect Homepage Title *************")
            self.driver.quit()
            self.logger.info("************ Test case Failed *************")


    def randomEmailGenerator(self):
        s = ''
        length = random.randint(1,10)
        for index in range(length):
            s = s + random.choice(string.ascii_letters)
        return s

    def randomFirstNameGenerator(self):
        s = ''
        length = random.randint(1,10)
        for index in range(length):
            s = s + random.choice(string.ascii_letters)
        return s

    def randomLastNameGenerator(self):
        s = ''
        length = random.randint(1,10)
        for index in range(length):
            s = s + random.choice(string.ascii_letters)
        return s

    def randomPasswordGenerator(self):
        s = ''
        length = random.randint(1,10)
        for index in range(length):
            s = s + random.choice(string.ascii_letters) + random.choice(string.digits)
        return s






