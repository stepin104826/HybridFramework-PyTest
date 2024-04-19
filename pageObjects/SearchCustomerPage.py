from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class SearchCustomerPage:
    customersMenu_xpath = ' /html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a'
    customersMenuOption_xpath = '//a[@href="/Admin/Customer/List"]'
    addNewButton_linktext = 'Add new'
    searchemailtextbox_id = "SearchEmail"
    searchfirstnametextbox_id = "SearchFirstName"
    searchlastnametextbox_id = "SearchLastName"
    searchdobmonth_id = "SearchMonthOfBirth"
    searchdobday_id = "SearchDayOfBirth"
    regfromdate_id = "SearchRegistrationDateFrom"
    regtodate_id = "SearchRegistrationDateTo"
    searchlastactfrom_id = "SearchLastActivityFrom"
    searchlastactto_id = "SearchLastActivityTo"
    searchcompany_name = "SearchCompany"
    searchipaddress_name = "SearchIpAddress"
    searchcustomerroles_xpath = "/html/body/div[3]/div[1]/form[1]/section/div/div/div/div[1]/div/div[2]/div[1]/div[2]/div[5]/div[2]/div/div"
    searchcustomersbutton_id = "search-customers"

    def __init__(self, driver):
        self.driver = driver

    def clickCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.customersMenu_xpath).click()

    def chooseCustomerOption(self):
        self.driver.find_element(By.XPATH, self.customersMenuOption_xpath).click()

    def enterCustEmail(self, email):
        self.driver.find_element(By.ID, self.searchemailtextbox_id).send_keys(email)

    def enterCustFirstName(self, fn):
        self.driver.find_element(By.ID, self.searchfirstnametextbox_id).send_keys(fn)

    def enterCustLastName(self, ln):
        self.driver.find_element(By.ID, self. searchlastnametextbox_id).send_keys(ln)

    def selectDOBMonth(self, month):
        select = Select(self.driver.find_element(By.ID, self.searchdobmonth_id))
        select.select_by_value(str(month))

    def selectDOBDay(self, day):
        select = Select(self.driver.find_element(By.ID, self.searchdobday_id))
        select.select_by_value(str(day))

    def selectRegFrom(self, date):
        self.driver.find_element(By.ID, self.regfromdate_id).send_keys(date)

    def selectRegTo(self, date):
        self.driver.find_element(By.ID, self.regtodate_id).send_keys(date)

    def selectlastActFrom(self, date):
        self.driver.find_element(By.ID, self.searchlastactfrom_id).send_keys(date)

    def selectlastActTo(self, date):
        self.driver.find_element(By.ID, self.searchlastactto_id).send_keys(date)

    def enterCompanyName(self, company):
        self.driver.find_element(By.NAME, self.searchcompany_name).send_keys(company)

    def enterIPAddress(self, ip):
        self.driver.find_element(By.NAME, self.searchipaddress_name).send_keys(ip)

    def enterCustomerRoles(self, role):
        self.driver.find_element(By.XPATH, self.searchcustomerroles_xpath).click()
        for ele in role:
            self.driver.find_element(By.XPATH, f'//li[contains(text(),"{ele}")]').click()

    def clickSearch(self):
        self.driver.find_element(By.ID, self.searchcustomersbutton_id).click()


