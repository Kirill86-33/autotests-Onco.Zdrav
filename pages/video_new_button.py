from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class VideoButtonNewPage(BasePage):
    PAGE_URL = 'https://onco.zdrav.mosreg.ru/library'

   
    BUTTON_NEW = ("xpath", "//div//button[text()='Новинки']") 
    



    def click_button_new(self):
        element = self.wait.until(EC.element_to_be_clickable(self.BUTTON_NEW))
        self.driver.execute_script("arguments[0].click();", element)