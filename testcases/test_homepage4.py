#click3 arravials image and check description of each image
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
        atb.chkdecriptionimage()
        print(atb.chkdecriptionimage())
        if 'Selenium WebDriver' in atb.chkdecriptionimage():
            hp.clickhome()
            hp.clckimage2()
            atb.chkdecriptionimage()
            print(atb.chkdecriptionimage())
            if 'This book provides you with an ' in atb.chkdecriptionimage():
                hp.clickhome()
                hp.clckimage3()
                atb.chkdecriptionimage()
                print(atb.chkdecriptionimage())
                if 'It would seem that everything that needs' in atb.chkdecriptionimage():
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


