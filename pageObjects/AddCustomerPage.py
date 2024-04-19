import random
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class AddCustomerPage:
    customersMenu_xpath = ' /html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a'
    customersMenuOption_xpath = '//a[@href="/Admin/Customer/List"]'
    addNewButton_linktext = 'Add new'
    emailtextbox_id = "Email"
    passwordtextbox_name = "Password"
    firstnametextbox_id = "FirstName"
    lastnametextbox_id = "LastName"
    genderradiobutton_baseid = "Gender_"
    dobtextbox_id =  "DateOfBirth"
    companytextbox_name = "Company"
    taxexemptcheckbox_id = "IsTaxExempt"
    newslettertextbox_xpath = "/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[9]/div[2]/div/div[1]/div/div"
    customerrolestextbox_xpath = "/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[10]/div[2]/div/div[1]/div/div"
    vendormanagerselectdd_id = "VendorId"
    activecheckbox_id = "Active"
    admincommenttextbox_id = "AdminComment"
    savebutton_xpath = '//button[@name="save"]'

    def __init__(self, driver):
        self.driver = driver

    def clickCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.customersMenu_xpath).click()

    def chooseCustomerOption(self):
        self.driver.find_element(By.XPATH, self.customersMenuOption_xpath).click()

    def clickAddNewButton(self):
        self.driver.find_element(By.LINK_TEXT, self.addNewButton_linktext).click()

    def enterCustEmail(self, email):
        self.driver.find_element(By.ID, self.emailtextbox_id).send_keys(email)

    def enterCustPassword(self, password):
        self.driver.find_element(By.NAME, self.passwordtextbox_name).send_keys(password)

    def enterCustFirstName(self, fn):
        self.driver.find_element(By.ID, self.firstnametextbox_id).send_keys(fn)

    def enterCustLastName(self, ln):
        self.driver.find_element(By.ID, self.lastnametextbox_id).send_keys(ln)

    def selectGender(self, gender):
        self.driver.find_element(By.ID, f'{self.genderradiobutton_baseid}'+f'{gender}').click()

    def selectDOB(self, dob):
        self.driver.find_element(By.ID, self.dobtextbox_id).send_keys(dob)

    def enterCompanyName(self, company):
        self.driver.find_element(By.NAME, self.companytextbox_name).send_keys(company)

    def checktaxexempt(self, check):
        if check:
            self.driver.find_element(By.ID, self.taxexemptcheckbox_id).click()
        else:
            pass

    def inputnewsletter(self, ele):
        self.driver.find_element(By.XPATH, self.newslettertextbox_xpath).click()
        self.driver.find_element(By.XPATH, f'//li[contains(text(),"{ele}")]').click()

    def inputCustomerRoles(self):
        self.driver.find_element(By.XPATH,'//*[@id="SelectedCustomerRoleIds_taglist"]/li/span[2]').click()
        sleep(2)
        self.driver.find_element(By.XPATH, self.customerrolestextbox_xpath).click()
        options = ["Registered","Guests"]
        ele = random.choice(options)
        self.driver.find_element(By.XPATH,f'//li[contains(text(),"{ele}")]').click()

    def selectVendorManager(self):
        select = Select(self.driver.find_element(By.ID, self.vendormanagerselectdd_id))
        value = random.choice(["Vendor 1","Vendor 2","Not a vendor"])
        # self.driver.find_element(By.ID, self.vendormanagerselectdd_id).click()
        select.select_by_visible_text(value)


    def checkActive(self):
        self.driver.find_element(By.ID, self.activecheckbox_id).click()

    def enterAdminComment(self, text):
        self.driver.find_element(By.ID, self.admincommenttextbox_id).clear()
        self.driver.find_element(By.ID, self.admincommenttextbox_id).send_keys(text)

    def clickSave(self):
        self.driver.find_element(By.XPATH, self.savebutton_xpath).click()
