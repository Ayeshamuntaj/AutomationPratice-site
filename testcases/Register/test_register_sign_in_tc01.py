# 1) Open the browser
# 2) Enter the URL “http://practice.automationtesting.in/”
# 3) Click on My Account Menu
# 4) Enter registered Email Address in Email-Address textbox
# 5) Enter your own password in password textbox
# 6) Click on Register button
# 7) User will be registered successfully and will be navigated to the Home page

from Pageobject.Register.page_registration import Registration
from Utilities.Readproperties import ReadConfig
from Utilities.randomemail import Randomemailgenerator

class TestRegisterSignin:
    def test_ResisterSignin(self,driver):
        driver.get(ReadConfig.getApplicationurl())
        driver.maximize_window()
        driver.registration=Registration(driver)
        driver.registration.myaccount_click().email_address_input(Randomemailgenerator.random_email_generator()+"@gmail.com").password_input("Test@testing1234").register_button_click()
        assert driver.registration.signout_link_displayed()=='Sign out',"Home page not loaded for Registration Signoff TC01 scenario"
        driver.close()
