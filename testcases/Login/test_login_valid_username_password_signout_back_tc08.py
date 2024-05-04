# 1) Open the browser
# 2) Enter the URL “http://practice.automationtesting.in/”
# 3) Click on My Account Menu
# 4) Enter registered username in username textbox
# 5) Enter password in password textbox
# 6) Click on login button
# 7) User must successfully login to the web page
from Pageobject.Login.page_login import Login
from Utilities.Readproperties import ReadConfig
class TestLogin:
    def test_Login(self,driver):
        login=Login(driver)
        login.selenium.openurl_max(ReadConfig.getApplicationurl())
        login.myaccount_click().username_input("test.demo@testing.com").password_input("Test@testing1234").login_button_click().signout_click()
        assert login.login_button_enabled(),"Home page not loaded for Login Signoff TC01 scenario"
        login.close()
