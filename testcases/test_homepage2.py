import os.path
from selenium import webdriver
from Pageobject.homepage import Homepage
from Utilities.Readproperties import ReadConfig
from Utilities.selenium import selenium
class Testhomepagearrival:
    def test_homepagearrival(self,driver):
        driver.get(ReadConfig.getApplicationurl())
        driver.maximize_window()
        #object for homepage
        hp = Homepage(driver)
        hp.clickshop()
        hp.clickhome()
        arrivalcount=hp.arrivalcount()
        print(f"No of arraivals = {arrivalcount}")
        #object for selenium
        se=selenium(driver)
        if arrivalcount ==3:
            se.allurerepo()
            assert True
        else:
            assert False



