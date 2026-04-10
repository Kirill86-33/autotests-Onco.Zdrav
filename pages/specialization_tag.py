from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
class TegSpecializations(BasePage):
    PAGE_URL = 'https://onco.zdrav.mosreg.ru/clinics'


    BLOCK_SPECIALIZATION = ("xpath", "//div//span[text()='круглосуточный стационар']") 
 

    def click_tag(self):
        element = self.wait.until(EC.element_to_be_clickable(self.BLOCK_SPECIALIZATION))
        self.driver.execute_script("arguments[0].click();", element)