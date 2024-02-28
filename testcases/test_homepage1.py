import os.path

from selenium import webdriver
from Pageobject.homepage import Homepage
from Utilities.Readproperties import ReadConfig
from Utilities.selenium import selenium

class Testhomegeslider:
    def test_homepageslider(self,driver):
        driver.get(ReadConfig.getApplicationurl())
        driver.maximize_window()
        #object created for homepage
        hp=Homepage(driver)
        #object created for selenium
        sel=selenium(driver)
        hp.clickshop()
        hp.clickhome()
        clicks=hp.sliderpagecount()
        if clicks ==3:
            print(f" No of sliders = {clicks}")
            sel.allurerepo()
            sel.quit()
            assert True
        else:
            sel.quit()
            assert False


