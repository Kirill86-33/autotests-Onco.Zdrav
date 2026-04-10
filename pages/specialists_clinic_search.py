from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
class DoctorsSearchClinic(BasePage):
    PAGE_URL = 'https://onco.zdrav.mosreg.ru/doctors'


    SEARCH_FIELD_CLINIC = ("xpath", "//div//input[@placeholder='Поиск по клинике']") 
    BUTTON_CLINIC = ("xpath", "//div//span[text()='ГБУЗ Московской области «Волоколамская больница»']") 

    def wait_for_page_load(self):
        self.wait.until(EC.visibility_of_element_located(self.SEARCH_FIELD_CLINIC))


   
    def enter_input_search_clinic(self, city):
        self.wait_for_page_load()
        input_city = self.wait.until(EC.element_to_be_clickable(self.SEARCH_FIELD_CLINIC))
        input_city.clear()
        input_city.send_keys(city)



    def click_button_city(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.BUTTON_CLINIC))
        self.driver.execute_script("arguments[0].click();", btn)