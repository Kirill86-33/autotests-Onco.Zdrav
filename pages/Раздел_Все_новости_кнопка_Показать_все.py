from pages.base_page import BasePage

class ButtonShowAll(BasePage):
    PAGE_URL = 'https://onco.zdrav.mosreg.ru/news'


    BUTTON_SHOW_ALL = ("xpath", "//div//button[text()='Показать все']") 
                                               


    def click_button_show_all (self):  
       button_show_all = self.driver.find_element(*self.BUTTON_SHOW_ALL) # Добавляем явное ожидание
       self.driver.execute_script("arguments[0].click();", button_show_all)
