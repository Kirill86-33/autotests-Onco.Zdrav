from pages.base_page import BasePage

class NewsSearchPage(BasePage):
    PAGE_URL = 'https://onco.zdrav.mosreg.ru/news'


    SEARCH_FIELD = ("xpath", "//div//input[@placeholder='Поиск']")
    CART_VIDEO = ("xpath", "(//div//a[@itemtype='https://schema.org/Movie'])[1]")




    def enter_input_search (self, text):  
       input_search = self.driver.find_element(*self.SEARCH_FIELD) # Добавляем явное ожидание
       input_search.send_keys(text)



    def click_cart_news (self):  
        cart_news = self.driver.find_element(*self.CART_VIDEO) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", cart_news)