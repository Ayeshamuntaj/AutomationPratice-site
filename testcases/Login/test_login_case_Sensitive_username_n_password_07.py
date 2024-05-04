# 1) Open the browser
# 2) Enter the URL “http://practice.automationtesting.in/”
# 3) Click on My Account Menu
# 4) Enter the case changed username in username textbox
# 5) Enter the case chenged password in the password tetxbox
# 6) Now click on login button
# 7) Login must fail saying incorrect username/password.
from Pageobject.Login.page_login import Login
from Utilities.Readproperties import ReadConfig
class TestLogin:
    def test_Login(self,driver):
        login=Login(driver)
        login.selenium.openurl_max(ReadConfig.getApplicationurl())
        login.myaccount_click().case_sensitive_username_input("test.demo@testing.com").case_sensitive_password_input("Test@testing1234").login_button_click()
        assert login.invalid_Emaild_address_error_text()=='Error: The password you entered for the username TEST.DEMO@TESTING.COM is incorrect. Lost your password?',"Invalid credentials given for  Login Signoff TC07 scenario"
        login.close()
