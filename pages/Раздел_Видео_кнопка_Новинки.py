from pages.base_page import BasePage

class VideoButtonNewPage(BasePage):
    PAGE_URL = 'https://onco.zdrav.mosreg.ru/library'

   
    BUTTON_NEW = ("xpath", "//div//button[text()='Новинки']") 
    


    def click_button_new(self):  
        button_new = self.driver.find_element(*self.BUTTON_NEW) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", button_new)