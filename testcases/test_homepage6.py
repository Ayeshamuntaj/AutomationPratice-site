from time import sleep

from Pageobject.addtobasket import Addtobasket
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
        # object for addtobasket
        atb = Addtobasket(driver)
        if arrivalcount ==3:
            hp.clckimage1()
            atb.clckAddtocart()
            atb.chkmsgseleniumruby()
            atb.clckViewbasket()
            atb.chkprice()
            print(atb.chkprice())
            if "500" in atb.chkprice():
                hp.clickhome()
                hp.clckimage2()
                atb.clckAddtocart()
                atb.clckViewbasket()
                atb.chkprice()
                print(atb.chkchangedprice())
                if "400" in atb.chkchangedprice():
                    hp.clickhome()
                    hp.clckimage3()
                    atb.clckAddtocart()
                    atb.clckViewbasket()
                    atb.chkprice()
                    print(atb.chkprice())
                #     if atb.chkreviews() == True:
                #         se.quit()
                #         assert True
                #     else:
                #         se.allurerepo()
                #         se.quit()
                #         assert False
                # else:
                #     se.allurerepo()
                #     se.quit()
                #     assert False
