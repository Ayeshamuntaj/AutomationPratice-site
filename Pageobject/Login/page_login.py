import string

from Utilities.selenium import selenium
from selenium.webdriver.common.by import By

class Login:
    def __init__(self, driver):
        self.selenium = selenium(driver)

    #locators:
    MY_ACCOUNT_XPATH="//a[text()='My Account']"
    USER_NAME_INPUT_ID="username"
    PASSWORD_INPUT_ID="password"
    LOGIN_BUTTON_NAME="login"
    SIGN_OUT_LINK_DISPLAYED_XPATH="//a[text()='Sign out']"
    ERROR_MESSAGE_INVALID_EMAIL_ADDRESS_XPATH="//ul[@class='woocommerce-error']/li"
    #action methos

    def myaccount_click(self):
        self.selenium.click(By.XPATH,self.MY_ACCOUNT_XPATH)
        return self

    def username_input(self,emailaddress):
        self.selenium.type(By.ID,self.USER_NAME_INPUT_ID,emailaddress)
        return self

    def password_input(self,password):
        self.selenium.type(By.ID,self.PASSWORD_INPUT_ID,password)
        return self

    def login_button_click(self):
        self.selenium.click(By.NAME,self.LOGIN_BUTTON_NAME).sleepforseconds(2)
        return self

    def login_button_enabled(self):
        self.selenium.is_enabled(By.NAME,self.LOGIN_BUTTON_NAME)
        return self

    def signout_link_displayed(self):
        return self.selenium.getelementtext(By.XPATH,self.SIGN_OUT_LINK_DISPLAYED_XPATH)

    def signout_click(self):
        self.selenium.click(By.XPATH,self.SIGN_OUT_LINK_DISPLAYED_XPATH).sleepforseconds(2)
        self.selenium.back()
        return self

    def invalid_Emaild_address_error_text(self):
        return self.selenium.getelementtext(By.XPATH,self.ERROR_MESSAGE_INVALID_EMAIL_ADDRESS_XPATH)

    def password_invalid(self):
        return self.selenium.findelement(By.ID,self.PASSWORD_INPUT_ID).get_attribute("value")

    def close(self):
        return self.selenium.quit()

    def case_sensitive_username_input(self,emailaddress):
        uppercase_emailaddress=emailaddress.upper()
        self.selenium.type(By.ID,self.USER_NAME_INPUT_ID,uppercase_emailaddress)
        return self

    def case_sensitive_password_input(self,password):
        uppercase_password=password.upper()
        self.selenium.type(By.ID,self.PASSWORD_INPUT_ID,uppercase_password)
        return self