# 1) Open the browser
# 2) Enter the URL “http://practice.automationtesting.in/”
# 3) Click on My Account Menu
# 4) Enter empty Email Address in Email-Address textbox
# 5) Enter empty password in password textbox
# 6) Click on Register button
# # 7) Registration must fail with a warning message(ie please provide valid email address)

from Pageobject.Register.page_registration import Registration
from Utilities.Readproperties import ReadConfig
from Utilities.randomemail import Randomemailgenerator

class TestRegisterSigninError:
    def test_ResisterSignin_error_invalid_Emailid(self,driver):
        registration=Registration(driver)
        registration.selenium.openurl_max(ReadConfig.getApplicationurl())
        registration.myaccount_click().email_address_input("").password_input("").register_button_click()
        assert registration.invalid_Emaild_address_error_text()=='Error: Please provide a valid email address.',"Error message not displayed when empty email and password given for Registration Signoff TC04 scenario"
        registration.close()