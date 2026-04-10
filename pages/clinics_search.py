from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
class MedicalOrganizationsSearch(BasePage):
    PAGE_URL = 'https://onco.zdrav.mosreg.ru/clinics'

  
    SEARCH_FIELD = ("xpath", "//div//input[@placeholder='Поиск']")  
    CART_LPU = ("xpath", "//div//h4[text()='ГБУЗ Московской области «Волоколамская больница»']")




    def enter_input_search(self, text):
        field = self.wait.until(EC.visibility_of_element_located(self. SEARCH_FIELD))
        field.clear()
        field.send_keys(text)




    def click_cart_lpu(self):
        card = self.wait.until(EC.element_to_be_clickable(self.CART_LPU))
        self.driver.execute_script("arguments[0].click();", card)