import random
import string

from Utilities.selenium import selenium
from selenium.webdriver.common.by import By

class Homepage:
    def __init__(self, driver):
        self.selenium = selenium(driver)

    #locators:
    SHOP_LINK_XPATH="//ul[@id='main-nav']/li/a[text()='Shop']"
    HOME_PAGE_LINK="//nav[@class='woocommerce-breadcrumb']/a"
    SLIDER_COUNT="//div[@class='n2-ss-slider-3']/div"
    ARRIVAL_COUNT="//div[contains(@class,'default   sub_row_1-0-2')]/div"
    ADD_TO_BASKET_BUTTON="//button[@type='submit']"
    CART_ITEMS_COUNT="//span[@class='cartcontents']"
    PRODUCT_DESCRIPTION_DISPLAYED="//div[@id='tab-description']/p"
    REVIEWS_TAB = "//a[normalize-space()='Reviews (0)']"
    REVIEWS_TEXT_DISPLAYED="//div[@id='comments']/p"
    AMOUNT_ADD_TO_CART="//a[@title='View your shopping cart']/span[2]"
    ITEM_ADD_TO_CART="//a[@title='View your shopping cart']/span[1]"
    ADD_TO_BASKET_INPUT= "//input[@class='input-text qty text']"
    SELENIUM_BOOK="//div[@id='text-22-sub_row_1-0-2-0-0']"
    TOTAL_AMOUNT="//li[@id='wpmenucartli']/a/span[2]"
    PROCEED_TO_CHECK_OUT="//div[@class='wc-proceed-to-checkout']/a"
    BILLING_DETAILS_TITLE="//h3[contains(text(),'Billing Details')]"
    COUPON_CODE_INPUT="//input[@id='coupon_code']"
    SUB_TOTAL_AMOUNT="//tr[@class='cart-subtotal']/td/span/span"
    APPLY_COUPON_BUTTON="//input[@name='apply_coupon']"
    COUPON_CODE_APPLIED_AMOUNT="//td[@data-title='Coupon: krishnasakinala']/span"
    TOTAL_AMOUNT_POST_COUPON="//tr[@class='order-total']/td[@data-title='Total']/strong/span[@class='woocommerce-Price-amount amount']"

    #action methos

    def shop_link(self):
        self.selenium.click(By.XPATH,self.SHOP_LINK_XPATH)
        return self

    def homepage_link(self):
        self.selenium.click(By.XPATH,self.HOME_PAGE_LINK)
        return self

    def slider_count(self):
        slider=self.selenium.findelements(By.XPATH,self.SLIDER_COUNT)
        for element in slider:
            count=len(slider)
            return count

    def arrival_count(self):
        arrival=self.selenium.findelements(By.XPATH,self.ARRIVAL_COUNT)
        count=len(arrival)
        return count

    def arrival_add_to_basket_all_images(self):
        arrival = self.selenium.findelements(By.XPATH, self.ARRIVAL_COUNT)
        for element in arrival:
            self.selenium.click(By.XPATH,self.ARRIVAL_COUNT).sleepforseconds(2).click(By.XPATH,self.ADD_TO_BASKET_BUTTON).click(By.XPATH,self.HOME_PAGE_LINK)
        return self

    def cart_item_count(self):
        return self.selenium.getelementtext(By.XPATH,self.CART_ITEMS_COUNT)

    def product_description(self):
        arrival = self.selenium.findelements(By.XPATH, self.ARRIVAL_COUNT)
        for element in arrival:
            self.selenium.click(By.XPATH, self.ARRIVAL_COUNT).sleepforseconds(2).click(By.XPATH,self.ADD_TO_BASKET_BUTTON).sleepforseconds(1)
            self.selenium.scrolldown()
            if self.selenium.is_displayed(By.XPATH,self.PRODUCT_DESCRIPTION_DISPLAYED):
                self.selenium.scrollup().click(By.XPATH,self.HOME_PAGE_LINK)
        return self

    def product_review(self):
        arrival = self.selenium.findelements(By.XPATH, self.ARRIVAL_COUNT)
        for element in arrival:
            self.selenium.click(By.XPATH, self.ARRIVAL_COUNT).sleepforseconds(2).click(By.XPATH,self.ADD_TO_BASKET_BUTTON).sleepforseconds(1)
            self.selenium.scrolldown().sleepforseconds(1)
            self.selenium.wait_by_visible(By.XPATH,self.REVIEWS_TAB).click()
            self.selenium.sleepforseconds(1).scrollup()
            if self.selenium.is_displayed(By.XPATH,self.REVIEWS_TEXT_DISPLAYED):
                self.selenium.click(By.XPATH,self.HOME_PAGE_LINK)
        return self

    def add_to_cart_amount(self):
        arrival = self.selenium.findelements(By.XPATH, self.ARRIVAL_COUNT)
        Amount=['₹500.00','₹400.00','₹350.00']
        for element in arrival:
            self.selenium.click(By.XPATH, self.ARRIVAL_COUNT).sleepforseconds(2).click(By.XPATH,self.ADD_TO_BASKET_BUTTON).click(By.XPATH, self.HOME_PAGE_LINK)
        return self

    def add_to_cart_books(self,bookscount):
        self.selenium.scroll_element(By.XPATH,self.ARRIVAL_COUNT)
        self.selenium.click(By.XPATH,self.SELENIUM_BOOK).clear(By.XPATH,self.ADD_TO_BASKET_INPUT).type(By.XPATH,self.ADD_TO_BASKET_INPUT,bookscount).click(By.XPATH,self.ADD_TO_BASKET_BUTTON)
        return self.selenium.getelementtext(By.XPATH,self.ITEM_ADD_TO_CART)

    def total_amount_validation(self):
        return self.selenium.getelementtext(By.XPATH,self.TOTAL_AMOUNT)

    def proceed_to_check_out(self):
        self.selenium.click(By.XPATH,self.TOTAL_AMOUNT)
        self.selenium.scroll_element(By.XPATH,self.PROCEED_TO_CHECK_OUT).wait_by_visible(By.XPATH,self.PROCEED_TO_CHECK_OUT).click()
        return self.selenium.getelementtext(By.XPATH,self.BILLING_DETAILS_TITLE)

    def apply_coupon_code(self,couponcode):
        self.selenium.click(By.XPATH, self.TOTAL_AMOUNT).click(By.XPATH,self.COUPON_CODE_INPUT)
        self.selenium.type(By.XPATH,self.COUPON_CODE_INPUT,couponcode).sleepforseconds(2)
        self.selenium.click(By.XPATH,self.APPLY_COUPON_BUTTON).sleepforseconds(2).scroll_element(By.XPATH,self.COUPON_CODE_APPLIED_AMOUNT)
        return self.selenium.getelementtext(By.XPATH,self.COUPON_CODE_APPLIED_AMOUNT)

    def sub_total_amount(self):
        return self.selenium.getelementtext(By.XPATH,self.SUB_TOTAL_AMOUNT)
    def total_amount_post_coupon_code(self):
        total_amount_element = self.selenium.findelement(By.XPATH,self.TOTAL_AMOUNT_POST_COUPON)
        if total_amount_element:
            return total_amount_element.text.strip()  # Get the text content of the element and strip any leading/trailing whitespace
        else:
            return None



