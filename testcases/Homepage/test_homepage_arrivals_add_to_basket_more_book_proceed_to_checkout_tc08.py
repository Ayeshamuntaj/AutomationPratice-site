# 1) Open
# the
# browser
# 2) Enter
# the
# URL “http: // practice.automationtesting. in / ”
# 3) Click
# on
# Shop
# Menu
# 4) Now
# click
# on
# Home
# menu
# button
# 5) Test
# whether
# the
# Home
# page
# has
# Three
# Arrivals
# only
# 6) The
# Home
# page
# must
# contains
# only
# three
# Arrivals
# 7) Now
# click
# the
# image in the
# Arrivals
# 8) Test
# whether
# it is navigating
# to
# next
# page
# where
# the
# user
# can
# add
# that
# book
# into
# his
# basket.
# 9) Image
# should
# be
# clickable and shoul
# navigate
# to
# next
# page
# where
# user
# can
# add
# that
# book
# to
# his
# basket
# 10) Click
# on
# the
# Add
# To
# Basket
# button
# which
# adds
# that
# book
# to
# your
# basket
# 11) User
# can
# view
# that
# Book in the
# Menu
# item
# with price.
# 12) Now click on Item link which navigates to proceed to check out page.
# 13) User can click on the Item link in menu item after adding the book in to the basket which leads to the check out page
import time

from Pageobject.Homepage.page_homepage import Homepage
from Utilities.Readproperties import ReadConfig
class TestHomepagearrivalsproceedtocheckout:
    def test_homepage_proceed_to_checkout(self,driver):
        homepage=Homepage(driver)
        homepage.selenium.openurl_max(ReadConfig.getApplicationurl())
        homepage.shop_link().homepage_link()
        assert homepage.arrival_count()==3,"Arrival count displayed incorrect for the Homepage arrival count scenario"
        homepage.add_to_cart_books('1')
        assert homepage.cart_item_count() == "1 Item", "No. of books are not added correctly for Test scenarios 7"
        assert homepage.total_amount_validation()=="₹500.00","Amount is displayed incorrectly"
        assert homepage.proceed_to_check_out()=='Billing Details',"Billing Details page not displayed post checkout"

