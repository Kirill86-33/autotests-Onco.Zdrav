from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
class TegNewsPage(BasePage):
    PAGE_URL = 'https://onco.zdrav.mosreg.ru/news'


    NEWS_BLOCK_TEG = ("xpath", "(//div//span[text()='Советы врачей'])[1]") 
    CART_VIDEO = ("xpath", "//div//h4[text()='Позаботьтесь о главном: приглашаем на День здоровья в центры онкологической помощи']")



    def wait_for_page_load(self):
        self.wait.until(EC.visibility_of_element_located(self.NEWS_BLOCK_TEG))


    def click_teg_news  (self):
        self.wait_for_page_load()
        element = self.wait.until(EC.element_to_be_clickable(self.NEWS_BLOCK_TEG))
        self.driver.execute_script("arguments[0].click();", element)



    def click_cart_news (self):
        element = self.wait.until(EC.element_to_be_clickable(self.CART_VIDEO))
        self.driver.execute_script("arguments[0].click();", element)
