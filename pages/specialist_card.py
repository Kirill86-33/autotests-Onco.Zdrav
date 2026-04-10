from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
class SpecialistsCart(BasePage):
    PAGE_URL = 'https://onco.zdrav.mosreg.ru/doctors'

    CART_SPECIALISTS = ("xpath", "//div//h4[text()='Жукова Елена Николаевна']") 
  



    def click_cart_specialists (self):
        element = self.wait.until(EC.element_to_be_clickable(self.CART_SPECIALISTS))
        self.driver.execute_script("arguments[0].click();", element)