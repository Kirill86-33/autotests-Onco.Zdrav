from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
class DoctorsSearch(BasePage):
    PAGE_URL = 'https://onco.zdrav.mosreg.ru/doctors'

  
    SEARCH_FIELD = ("xpath", "//div//input[@placeholder='Поиск']")
    CART_SPECIALIST = ("xpath", "//div//h4[text()='Лядов Константин Викторович']")


    def wait_for_page_load(self):
        self.wait.until(EC.visibility_of_element_located(self.SEARCH_FIELD))



    def enter_input_search  (self, city):
        self.wait_for_page_load()
        input_city = self.wait.until(EC.element_to_be_clickable(self.SEARCH_FIELD))
        input_city.clear()
        input_city.send_keys(city)



    def click_cart_specialist(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.CART_SPECIALIST))
        self.driver.execute_script("arguments[0].click();", btn)