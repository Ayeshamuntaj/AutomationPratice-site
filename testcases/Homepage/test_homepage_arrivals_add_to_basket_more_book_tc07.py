# 1) Open the browser
# 2) Enter the URL “http://practice.automationtesting.in/”
# 3) Click on Shop Menu
# 4) Now click on Home menu button
# 5) Test whether the Home page has Three Arrivals only
# 6) The Home page must contains only three Arrivals
# 7) Now click the image in the Arrivals
# 8) Test whether it is navigating to next page where the user can add that book into his basket.
# 9) Image should be clickable and shoul navigate to next page where user can add that book to his basket
# 10) Click on the Add To Basket button which adds that book to your basket
# 11) User can view that Book in the Menu item with price.
# 12) User can add a book by clicking on Add To Basket button which adds that book in to his Basket
import time

from Pageobject.Homepage.page_homepage import Homepage
from Utilities.Readproperties import ReadConfig
class TestHomepagearrivalsamountvalidate:
    def test_homepage_validate_Amount(self,driver):
        homepage=Homepage(driver)
        homepage.selenium.openurl_max(ReadConfig.getApplicationurl())
        homepage.shop_link().homepage_link()
        assert homepage.arrival_count()==3,"Arrival count displayed incorrect for the Homepage arrival count scenario"
        homepage.add_to_cart_amount()
        assert homepage.cart_item_count() == "3 Items", "Add to cart not working for Images navigation under arrival page"
