from pages.base_page import BasePage

class SpecialistsCart(BasePage):
    PAGE_URL = 'https://onco.zdrav.mosreg.ru/doctors'

    CART_SPECIALISTS = ("xpath", "//div//h4[text()='Жукова Елена Николаевна']") 
  

    def click_cart_specialists(self):  
        cart_specialists = self.driver.find_element(*self.CART_SPECIALISTS) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", cart_specialists)