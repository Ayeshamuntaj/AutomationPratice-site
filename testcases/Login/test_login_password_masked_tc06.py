# 1) Open the browser
# 2) Enter the URL “http://practice.automationtesting.in/”
# 3) Click on My Account Menu
# 4) Enter the password field with some characters.
# 5) The password field should display the characters in asterisks or bullets such that the password is not visible on the screen

from Pageobject.Login.page_login import Login
from Utilities.Readproperties import ReadConfig
class TestLogin:
    def test_Login(self,driver):
        login=Login(driver)
        login.selenium.openurl_max(ReadConfig.getApplicationurl())
        login.myaccount_click().username_input("test.demo@testing.com").password_input("test.demo@testing.com")
        assert login.password_invalid()=='test.demo@testing.com',"Password field not is updated for TC-06"
        login.close()
