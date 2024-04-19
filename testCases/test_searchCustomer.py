import string
import random
from time import sleep

import pytest
from selenium.webdriver.common.by import By

from pageObjects.SearchCustomerPage import SearchCustomerPage
from utilities.customLogger import LogGeneration
from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomerPage


class Test_004_SearchCustomer:
    pageURL = ReadConfig.getApplicationURL()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()

    logger = LogGeneration.logGen()

    @pytest.mark.smoke
    def test_searchCustomer(self,setup):
        self.logger.info("********************* Test_004_SearchCustomers ***************************")

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
            self.logger.info("************ Verifying Search Customer Option *************")
            scObject = SearchCustomerPage(self.driver)
            scObject.clickCustomerMenu()
            scObject.chooseCustomerOption()

            search_criteria = ["name", "email", "company"]
            chosen = random.choice(search_criteria)

            if chosen  == "name":
                self.logger.info(f"************ Searching Customer by {chosen} *************")
                registered_fullnames = self.driver.find_elements(By.XPATH, '//tr[@class="odd"]//td[3]')
                first_names = []
                last_names = []
                for ele in registered_fullnames:
                    print(ele)
                    first_names.append((ele.text).split(" ")[0])
                    last_names.append((ele.text).split(" ")[1])
                fn_to_search = random.choice(first_names)
                ln_to_search = random.choice(last_names)
                scObject.enterCustFirstName(fn_to_search)
                scObject.enterCustLastName(ln_to_search)
                sleep(3)
                scObject.clickSearch()
                sleep(3)
                for i in range(2, 5):
                    search_result = self.driver.find_element(By.XPATH, f'//tr[@class="odd"]//td[{i}]')
                    print(search_result.text)
                    self.logger.info(f"************ {search_result.text} *************")
                sleep(3)
                self.driver.save_screenshot(".\\Screenshots\\" + "Search_results_test.png")
                sleep(3)
                self.logger.info("************ Test case Passed *************")
                self.driver.quit()

            elif chosen == "email":
                self.logger.info(f"************ Searching Customer by {chosen} *************")
                registered_emails = self.driver.find_elements(By.XPATH, '//tr[@class="odd"]//td[2]')
                emails_text = []
                for object in registered_emails:
                    emails_text.append(object.text)
                email_to_search = random.choice(emails_text)
                scObject.enterCustEmail(email_to_search)
                sleep(3)
                scObject.clickSearch()
                sleep(3)
                for i in range(2,5):
                    search_result = self.driver.find_element(By.XPATH, f'//tr[@class="odd"]//td[{i}]')
                    print(search_result.text)
                    sleep(3)
                    self.logger.info(f"************ {search_result.text} *************")
                self.driver.save_screenshot(".\\Screenshots\\" + "Search_results_test.png")
                sleep(3)
                self.logger.info("************ Test case Passed *************")
                self.driver.quit()

            elif chosen == "company":
                self.logger.info(f"************ Searching Customer by {chosen} *************")
                registered_companies = self.driver.find_elements(By.XPATH, '//tr[@class="odd"]//td[5]')
                companies_text = []
                for object in registered_companies:
                    companies_text.append(object.text)
                company_to_search = random.choice(companies_text)
                scObject.enterCompanyName(company_to_search)
                sleep(3)
                scObject.clickSearch()
                sleep(3)
                for i in range(2,5):
                    search_result = self.driver.find_element(By.XPATH, f'//tr[@class="odd"]//td[{i}]')
                    print(search_result.text)
                    self.logger.info(f"************ {search_result.text} *************")
                self.driver.save_screenshot(".\\Screenshots\\" + "Search_results_test.png")
                self.logger.info("************ Test case Passed *************")
                self.driver.quit()
        else:
            self.logger.info("************ Incorrect Homepage Title *************")
            self.driver.quit()
            self.driver.save_screenshot(".\\Screenshots\\" + "Search_results_test.png")
            self.logger.info("*********** Test case Failed *************")