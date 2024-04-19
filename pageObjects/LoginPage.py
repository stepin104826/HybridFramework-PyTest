from selenium.webdriver.common.by import By

class LoginPage:

    Email_textbox_id = 'Email'
    Password_textbox_id = 'Password'
    Login_button_xpath = '//button[@type="submit"]'
    Logout_button_linktext = 'Logout'

    def __init__(self,driver):
        self.driver = driver

    def enterEmail(self,inp):
        self.driver.find_element(By.ID, self.Email_textbox_id).clear()
        self.driver.find_element(By.ID, self.Email_textbox_id).send_keys(inp)

    def enterPassword(self,inp):
        self.driver.find_element(By.ID, self.Password_textbox_id).clear()
        self.driver.find_element(By.ID, self.Password_textbox_id).send_keys(inp)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.Login_button_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.Logout_button_linktext).click()

