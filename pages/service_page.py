from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
class ChapterService(BasePage):
    PAGE_URL = 'https://onco.zdrav.mosreg.ru/'

    CHAPTER_SERVICE = ("xpath", "//*[@id='__next']/main/div/div[2]/div[1]/div[3]/div[3]/a/h4")
    CARD_INPATIENT_CARE = ("xpath", "//div//h4[text()='Профилактика']")
 
  
    def click_chapter_service(self):
        element = self.wait.until(EC.presence_of_element_located(self.CHAPTER_SERVICE))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        clickable = self.wait.until(EC.element_to_be_clickable(self.CHAPTER_SERVICE))
        self.driver.execute_script("arguments[0].click();", clickable)


    def click_cart_inpatient_care(self):
        element = self.wait.until(EC.element_to_be_clickable(self.CARD_INPATIENT_CARE))
        self.driver.execute_script("arguments[0].click();", element)