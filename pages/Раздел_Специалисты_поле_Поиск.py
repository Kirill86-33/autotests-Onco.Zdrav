from pages.base_page import BasePage

class DoctorsSearch(BasePage):
    PAGE_URL = 'https://onco.zdrav.mosreg.ru/doctors'

  
    SEARCH_FIELD = ("xpath", "//div//input[@placeholder='Поиск']")




    def enter_input_search (self, text):  
       input_search = self.driver.find_element(*self.SEARCH_FIELD) # Добавляем явное ожидание
       input_search.send_keys(text)