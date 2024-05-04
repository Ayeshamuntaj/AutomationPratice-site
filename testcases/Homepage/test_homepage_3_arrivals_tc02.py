# 1) Open the browser
# 2) Enter the URL “http://practice.automationtesting.in/”
# 3) Click on Shop Menu
# 4) Now click on Home menu button
# 5) Test whether the Home page has Three Sliders only
# 6) The Home page must contains only three sliders
from Pageobject.Homepage.page_homepage import Homepage
from Utilities.Readproperties import ReadConfig
class TestHomepagesliderscount:
    def test_homepage_sliders_count(self,driver):
        homepage=Homepage(driver)
        homepage.selenium.openurl_max(ReadConfig.getApplicationurl())
        homepage.shop_link().homepage_link()
        assert homepage.slider_count()==3,"Slider count displayed incorrect for the Homepage slider count scenario"
        homepage.close()
