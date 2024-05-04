# 1) Open the browser
# 2) Enter the URL “http://practice.automationtesting.in/”
# 3) Click on My Account Menu
# 4) Enter registered username in username textbox
# 5) Enter password in password textbox
# 6) Click on login button
# 7) User must successfully login to the web page
# 8) Click on Myaccount link which leads to Dashboard
# 9) User must view Dashboard of the site
from Pageobject.Myaccount_Dashboard.page_myaccount_dashboard import Myaccountdashboard
from Utilities.Readproperties import ReadConfig
class TestMyaccountDashboard:
    def test_myaccount_dashboard(self,driver):
        myaccountdashboard=Myaccountdashboard(driver)
        myaccountdashboard.selenium.openurl_max(ReadConfig.getApplicationurl())
        myaccountdashboard.myaccount_click().username_input("test.demo@testing.com").password_input("Test@testing1234").login_button_click().dashboard_click()
        assert myaccountdashboard.dashboard_text().strip()=='From your account dashboard you can view your recent orders, manage your shipping and billing addresses and edit your password and account details.',"Dashboard page not displayed for My account page"
        myaccountdashboard.close()
