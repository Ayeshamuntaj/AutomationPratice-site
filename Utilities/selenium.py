from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
import os.path
from time import sleep

class selenium:
    def __init__(self,driver):
        self.driver=driver

    def openurl_max(self,url):
        self.driver.get(url)
        self.driver.maximize_window()
        return self

    def back(self):
        self.driver.back()
        return self

    def is_enabled(self,by,value):
        return self.driver.find_element(by,value).is_enabled()

    def is_displayed(self,by,value):
        return self.driver.find_element(by,value).is_displayed()

    def findelement(self, by, value):
        return self.driver.find_element(by, value)
    def findelements(self, by, value):
        return self.driver.find_elements(by, value)
    def allurerepot(self):
        screenshot_path = os.path.join(os.curdir, "Screenshots", "homepage1.png")
        self.driver.save_screenshot(screenshot_path)
        allure.attach(screenshot_path, attachment_type=allure.attachment_type.PNG, extension='png')
    def quit(self):
        return self.driver.quit()

    def wait_by_visible(self, by, value):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((by, value)))

    def scrollup(self):
        self.driver.execute_script("window.scrollBy(0, -500);")
        return self

    def scrolldown(self):
        self.driver.execute_script("window.scrollBy(0, 500);")
        return self

    def scroll_element(self,by,value):
        element=self.driver.find_element(By.XPATH,value)
        script = "arguments[0].scrollIntoView();"
        self.driver.execute_script(script, element)
        return self

    def click(self,by,value):
        element = self.driver.find_element(by, value)
        element.click()
        return self

    def type(self,by,value,input_value):
        element=self.driver.find_element(by,value)
        element.clear()
        element.send_keys(input_value)
        return self

    def sleepforseconds(self,value):
        sleep(value)
        return self

    def getelementtext(self,by,value):
       return self.driver.find_element(by,value).text

    def clear(self,by,value):
        element = self.driver.find_element(by, value)
        element.clear()
        return self

