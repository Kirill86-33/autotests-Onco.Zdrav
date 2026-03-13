from pages.base_page import BasePage

class DoctorsSearchClinic(BasePage):
    PAGE_URL = 'https://onco.zdrav.mosreg.ru/doctors'


    SEARCH_FIELD_CLINIC = ("xpath", "//div//input[@placeholder='Поиск по клинике']") 
    BUTTON_CLINIC = ("xpath", "//div//span[text()='ГБУЗ Московской области «Волоколамская больница»']") 


    def enter_input_search_clinic (self, text):  
       input_search_clinic = self.driver.find_element(*self.SEARCH_FIELD_CLINIC) # Добавляем явное ожидание
       input_search_clinic.send_keys(text)



    def click_button_clinic (self):  
        button_clinic = self.driver.find_element(*self.BUTTON_CLINIC) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", button_clinic)