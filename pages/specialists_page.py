from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
class Specialists(BasePage):
    PAGE_URL = 'https://onco.zdrav.mosreg.ru/'

    CHAPTER_SPECIALISTS = ("xpath", "//div//h4[text()='Специалисты']") 
  


    def click_chapter_specialists (self):
        btn = self.wait.until(EC.element_to_be_clickable(self.CHAPTER_SPECIALISTS))
        self.driver.execute_script("arguments[0].click();", btn)