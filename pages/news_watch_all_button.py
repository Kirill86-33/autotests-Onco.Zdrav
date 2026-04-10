from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
class ButtonSeeAll(BasePage):
    PAGE_URL = 'https://onco.zdrav.mosreg.ru/'


    BUTTON_SEE_ALL = ("xpath","//div//a[text()='Смотреть все']") 
                                               


    def click_button_see_all (self):
        element = self.wait.until(EC.element_to_be_clickable(self.BUTTON_SEE_ALL))
        self.driver.execute_script("arguments[0].click();", element)