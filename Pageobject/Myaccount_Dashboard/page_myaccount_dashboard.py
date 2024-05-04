import string

from Utilities.selenium import selenium
from selenium.webdriver.common.by import By

class Myaccountdashboard:
    def __init__(self, driver):
        self.selenium = selenium(driver)

    #locators:
    MY_ACCOUNT_XPATH="//a[text()='My Account']"
    USER_NAME_INPUT_ID="username"
    PASSWORD_INPUT_ID="password"
    LOGIN_BUTTON_NAME="login"
    SIGN_OUT_LINK_DISPLAYED_XPATH="//a[text()='Sign out']"
    ERROR_MESSAGE_INVALID_EMAIL_ADDRESS_XPATH="//ul[@class='woocommerce-error']/li"
    DASHBOARD_LINK_XPATH="//a[text()='Dashboard']"
    DASHBOARD_TEXT_XPATH="//div[@class='woocommerce-MyAccount-content']/p[2]"
    ORDERS_LINK_XPATH="//a[text()='Orders']"
    ORDERS_GO_SHOP_BUTTON_ENABLED_XPATH="//div[@class='woocommerce-Message woocommerce-Message--info woocommerce-info']/a"
    ADD_TO_BASKET_BUTTON_XPATH="//li[contains(@class,'post-170 product type')]//a[2]"

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

    def close(self):
        return self.selenium.quit()

    def dashboard_click(self):
        self.selenium.click(By.XPATH,self.DASHBOARD_LINK_XPATH)

    def dashboard_text(self):
        return self.selenium.getelementtext(By.XPATH,self.DASHBOARD_TEXT_XPATH)

    def orders_click(self):
        self.selenium.click(By.XPATH,self.ORDERS_LINK_XPATH)

    def orders_go_shop_enabled(self):
        return self.selenium.is_enabled(By.XPATH,self.ORDERS_GO_SHOP_BUTTON_ENABLED_XPATH)
