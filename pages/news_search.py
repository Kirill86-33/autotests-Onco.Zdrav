from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
class NewsSearchPage(BasePage):
    PAGE_URL = 'https://onco.zdrav.mosreg.ru/news'


    SEARCH_FIELD = ("xpath", "//div//input[@placeholder='Поиск']")
    CART_VIDEO = ("xpath", "//div//h4[text()='Не пугайтесь, это робот: голосовой помощник «Светлана» обзванивает пациентов']")



   
    def enter_input_search (self, text):
        field = self.wait.until(EC.visibility_of_element_located(self.SEARCH_FIELD))
        field.clear()
        field.send_keys(text)




    def click_cart_news (self):
        card = self.wait.until(EC.element_to_be_clickable(self.CART_VIDEO))
        self.driver.execute_script("arguments[0].click();", card)