from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
class ButtonShowAll(BasePage):
    PAGE_URL = 'https://onco.zdrav.mosreg.ru/news'


    BUTTON_SHOW_ALL = ("xpath", "//div//button[text()='Показать все']") 
                                               


    def click_button_show_all (self):
        element = self.wait.until(EC.element_to_be_clickable(self.BUTTON_SHOW_ALL))
        self.driver.execute_script("arguments[0].click();", element)