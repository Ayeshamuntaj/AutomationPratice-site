#click3 arravials image and add that book to the basket
import os.path
from selenium import webdriver
from Pageobject.homepage import Homepage
from Pageobject.addtobasket import Addtobasket
from Utilities.Readproperties import ReadConfig
from Utilities.selenium import selenium
class Testhomepgeaddtobasket:
    def test_homepageaddtobasket(self,driver):
        driver.get(ReadConfig.getApplicationurl())
        driver.maximize_window()
        #object for homepage
        hp = Homepage(driver)
        hp.clickshop()
        hp.clickhome()
       #object for addtobasket
        atb= Addtobasket(driver)
        #object creation for selenium
        se=selenium(driver)
        hp.clckimage1()
        atb.clckAddtocart()
        atb.clckViewbasket()
        print(atb.chkmsgseleniumruby())
        if '“Selenium Ruby” has been added to your basket.' in atb.chkmsgseleniumruby():
            hp.clickhome()
            hp.clckimage2()
            atb.clckAddtocart()
            atb.clckViewbasket()
            print(atb.chkmsgThinkingHTML())
            if 'Thinking in HTML” has been added to your basket.' in atb.chkmsgThinkingHTML():
                hp.clickhome()
                hp.clckimage3()
                atb.clckAddtocart()
                atb.clckViewbasket()
                print(atb.chkmsgJavascript())
                if '“Mastering JavaScript” has been added to your basket.' in atb.chkmsgJavascript():
                    se.allurerepo()
                    se.quit()
                    assert True
                else:
                    se.allurerepo()
                    se.quit()
                    assert False
            else:
                se.allurerepo()
                se.quit()
                assert False

        else:
            se.allurerepo()
            se.quit()
            assert False


