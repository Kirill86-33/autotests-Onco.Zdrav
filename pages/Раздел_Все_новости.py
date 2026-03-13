from pages.base_page import BasePage

class AllNewsPage(BasePage):
    PAGE_URL = 'https://onco.zdrav.mosreg.ru/'


    BUTTON_NEWS = ("xpath","(//div//a)[42]") 
   


    def click_button_news (self):  
        button_news = self.driver.find_element(*self.BUTTON_NEWS) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", button_news)


    