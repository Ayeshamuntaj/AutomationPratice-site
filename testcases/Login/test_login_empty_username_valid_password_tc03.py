# 1) Open the browser
# 2) Enter the URL “http://practice.automationtesting.in/”
# 3) Click on My Account Menu
# 4) Enter empty username in username textbox
# 5) Now enter valid password in the password textbox
# 6) Click on login button.
# 7) Proper error must be displayed(ie Invalid username) and prompt to enter login again
from Pageobject.Login.page_login import Login
from Utilities.Readproperties import ReadConfig
class TestLogin:
    def test_Login(self,driver):
        login=Login(driver)
        login.selenium.openurl_max(ReadConfig.getApplicationurl())
        login.myaccount_click().username_input("").password_input("Test@testing1234").login_button_click()
        assert login.invalid_Emaild_address_error_text()=='Error: Username is required.',"Home page not loaded for Login Signoff TC01 scenario"
        login.close()
