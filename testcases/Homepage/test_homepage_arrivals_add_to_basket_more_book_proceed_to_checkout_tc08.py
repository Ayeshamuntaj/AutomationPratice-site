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
# 13) Select more books than the books in stock.Ex if the stock has 20 books, try to add 21.
# 14) Click the add to basket button
# 15) Now it throws an error prompt like you must enter a value between 1 and 20
import time

from Pageobject.Homepage.page_homepage import Homepage
from Utilities.Readproperties import ReadConfig
class TestHomepagearrivalsaddmorebooks:
    def test_homepage_add_to_cart_more_books(self,driver):
        homepage=Homepage(driver)
        homepage.selenium.openurl_max(ReadConfig.getApplicationurl())
        homepage.shop_link().homepage_link()
        assert homepage.arrival_count()==3,"Arrival count displayed incorrect for the Homepage arrival count scenario"
        homepage.add_to_cart_more_books()
        assert homepage.cart_item_count() == "67890 Items", "No. of books are not added correctly for Test scenarios 7"
