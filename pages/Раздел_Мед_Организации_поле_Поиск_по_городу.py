from pages.base_page import BasePage

class MedicalSearchCity(BasePage):
    PAGE_URL = 'https://onco.zdrav.mosreg.ru/clinics'


    SEARCH_FIELD_CITY = ("xpath", "//div//input[@placeholder='Поиск по городу']") 
    BUTTON_CITY = ("xpath", "//div//span[text()='Волоколамск']") 


    def enter_input_search_city (self, text):  
       input_search_city = self.driver.find_element(*self.SEARCH_FIELD_CITY) # Добавляем явное ожидание
       input_search_city.send_keys(text)



    def click_button_city (self):  
        button_city = self.driver.find_element(*self.BUTTON_CITY) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", button_city)