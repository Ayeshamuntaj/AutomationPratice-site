from Utilities.selenium import selenium
from selenium.webdriver.common.by import By

class Registration:
    def __init__(self, driver):
        self.selenium = selenium(driver)

    #locators:
    MY_ACCOUNT_XPATH="//a[text()='My Account']"
    EMAIL_ADDRESS_INPUT_ID="reg_email"
    PASSWORD_INPUT_ID="reg_password"
    REGISTER_BUTTON_NAME="register"
    SIGN_OUT_LINK_DISPLAYED_XPATH="//a[text()='Sign out']"
    ERROR_MESSAGE_INVALID_EMAIL_ADDRESS_XPATH="//ul[@class='woocommerce-error']/li"
    #action methos

    def myaccount_click(self):
        self.selenium.click(By.XPATH,self.MY_ACCOUNT_XPATH)
        return self

    def email_address_input(self,emailaddress):
        self.selenium.type(By.ID,self.EMAIL_ADDRESS_INPUT_ID,emailaddress)
        return self

    def password_input(self,password):
        self.selenium.type(By.ID,self.PASSWORD_INPUT_ID,password)
        return self

    def register_button_click(self):
        self.selenium.click(By.NAME,self.REGISTER_BUTTON_NAME).sleepforseconds(2)
        return self

    def signout_link_displayed(self):
        return self.selenium.getelementtext(By.XPATH,self.SIGN_OUT_LINK_DISPLAYED_XPATH)

    def invalid_Emaild_address_error_text(self):
        return self.selenium.getelementtext(By.XPATH,self.ERROR_MESSAGE_INVALID_EMAIL_ADDRESS_XPATH)


    def close(self):
        return self.selenium.quit()
