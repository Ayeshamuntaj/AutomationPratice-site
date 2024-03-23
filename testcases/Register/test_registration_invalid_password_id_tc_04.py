# 1) Open the browser
# 2) Enter the URL “http://practice.automationtesting.in/”
# 3) Click on My Account Menu
# 4) Enter valid Email Address in Email-Address textbox
# 5) Enter empty password in password textbox
# 6) Click on Register button
# 7) Registration must fail with a warning message(ie please enter an account password)

from Pageobject.Register.page_registration import Registration
from Utilities.Readproperties import ReadConfig
from Utilities.randomemail import Randomemailgenerator

class TestRegisterSigninError:
    def test_ResisterSignin_error_invalid_Emailid(self,driver):
        driver.get(ReadConfig.getApplicationurl())
        driver.maximize_window()
        driver.registration=Registration(driver)
        driver.registration.myaccount_click().email_address_input(Randomemailgenerator.random_email_generator()+"@gmail.com").password_input("").register_button_click()
        assert driver.registration.invalid_Emaild_address_error_text()=='Error: Please enter an account password.',"Error message not displayed Empty password for Registration Signoff TC04 scenario"
        driver.close()