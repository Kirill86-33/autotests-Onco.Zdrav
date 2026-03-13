from pages.base_page import BasePage

class TegNewsPage(BasePage):
    PAGE_URL = 'https://onco.zdrav.mosreg.ru/news'


    NEWS_BLOCK_TEG = ("xpath", "(//div//span[text()='Советы врачей'])[1]") 
    CART_VIDEO = ("xpath", "(//div//a[@itemtype='https://schema.org/Movie'])[1]")



    def click_teg_news (self):  
        button_teg = self.driver.find_element(*self.NEWS_BLOCK_TEG) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", button_teg)


    def click_cart_news (self):  
        cart_news = self.driver.find_element(*self.CART_VIDEO) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", cart_news)