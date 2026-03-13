from pages.base_page import BasePage

class VideoSearchPage(BasePage):
    PAGE_URL = 'https://onco.zdrav.mosreg.ru/library'

    BUTTON_SEARCH = ("xpath", "//div//input[@placeholder='Поиск']") 
    SECTION_VIDEO = ("xpath", "(//div//h5)[1]")


  
    def enter_input_search (self, text):  
       input_search = self.driver.find_element(*self.BUTTON_SEARCH) # Добавляем явное ожидание
       input_search.send_keys(text)


    def click_button_section_video (self):  
        section_video = self.driver.find_element(*self.SECTION_VIDEO) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", section_video)