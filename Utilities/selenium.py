from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
import os.path

class selenium:
    def __init__(self,driver):
        self.driver=driver
    def findelement(self, by, value):
        return self.driver.find_element(by, value)
    def findelements(self, by, value):
        return self.driver.find_elements(by, value)
    def allurerepo(self):
        screenshot_path = os.path.join(os.curdir, "Screenshots", "homepage1.png")
        self.driver.save_screenshot(screenshot_path)
        allure.attach(screenshot_path, attachment_type=allure.attachment_type.PNG, extension='png')
    def quit(self):
        return self.driver.quit()

    def scrollup(self):
        self.driver.execute_script("window.scrollBy(0, -500);")