from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.selenium import selenium

class Addtobasket:
    #locators
    addtobasket_xpath=("//*[@class='single_add_to_cart_button button alt']",
                    "//*[@class='woocommerce-message']/a",
                    "//*[text()=' “Selenium Ruby” has been added to your basket.']",
                    "//*[text()=' “Thinking in HTML” has been added to your basket.']",
                    "//*[text()=' “Mastering JavaScript” has been added to your basket.']",
                    )
    #constructor
    def __init__(self,driver):
        self.driver=driver
        self.fe=selenium(driver)  #object created for findlement
    #action methods
    def clckAddtocart(self):
        self.fe.findelement(By.XPATH,self.addtobasket_xpath[0]).click()
    def clckViewbasket(self):
        return self.fe.findelement(By.XPATH,self.addtobasket_xpath[1]).is_enabled()
    def chkmsgseleniumruby(self):
        return self.fe.findelement(By.XPATH,self.addtobasket_xpath[2]).text
    def chkmsgThinkingHTML(self):
        return self.fe.findelement(By.XPATH,self.addtobasket_xpath[3]).text
    def chkmsgJavascript(self):
        return self.fe.findelement(By.XPATH,self.addtobasket_xpath[4]).text
