# 1) Open the browser
# 2) Enter the URL “http://practice.automationtesting.in/”
# 3) Click on My Account Menu
# 4) Enter incorrect username in username textbox
# 5) Enter incorrect password in password textbox.
# 6) Click on login button
# 7) Proper error must be displayed(ie Invalid username) and prompt to enter login again
from Pageobject.Login.page_login import Login
from Utilities.Readproperties import ReadConfig
class TestLogin:
    def test_Login(self,driver):
        login=Login(driver)
        login.selenium.openurl_max(ReadConfig.getApplicationurl())
        login.myaccount_click().username_input("test.demo@").password_input("34").login_button_click()
        assert login.invalid_Emaild_address_error_text()=="Error: The username test.demo@ is not registered on this site. If you are unsure of your username, try your email address instead.","Invalid username and password given for  Login Signoff TC02 scenario"
        login.close()
