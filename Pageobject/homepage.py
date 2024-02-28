from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.selenium import selenium


class Homepage:
    #locators
    homepage_xpath=("//*[@id='menu-item-40']/a",
                    "//*[@class='woocommerce-breadcrumb']/a",
                    "//*[@id='n2-ss-6']",
                    "//*[contains(@class,'n2-ss-slider-')]",
                    "//h2[text()='new arrivals']",
                    "//div[contains(@class, 'sub_column sub_column_1-0-2')]/div/div/ul/li",
                    "//ul[@class='products']/li",
                    "(//*[@class='woocommerce-LoopProduct-link'])[1]",
                    "(//*[@class='woocommerce-LoopProduct-link'])[2]",
                    "(//*[@class='woocommerce-LoopProduct-link'])[3]",
                    )
    #constructor
    def __init__(self,driver):
        self.driver=driver
        self.fe=selenium(driver)  #object created for findlement
    #action methods
    def clickshop(self):
        self.fe.findelement(By.XPATH,self.homepage_xpath[0]).click()
    def clickhome(self):
        self.fe.findelement(By.XPATH,self.homepage_xpath[1]).click()
    def sliderpagecount(self):
        self.fe.findelement(By.XPATH, self.homepage_xpath[2])
        sliders = self.fe.findelements(By.XPATH, self.homepage_xpath[3])
        count=0
        for slider in sliders:
            slider.click()
            count +=1
        return count
    def arrivalcount(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, self.homepage_xpath[4])))
        arrivals = self.fe.findelements(By.XPATH,self.homepage_xpath[5])
        count=0
        for arrival in arrivals:
            arrival.is_displayed()
            count +=1
        return count
    def clckimage1(self):
        self.fe.findelement(By.XPATH, self.homepage_xpath[7]).click()
    def clckimage2(self):
        self.fe.findelement(By.XPATH, self.homepage_xpath[8]).click()
    def clckimage3(self):
        self.fe.findelement(By.XPATH, self.homepage_xpath[9]).click()