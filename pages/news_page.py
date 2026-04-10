from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class AllNewsPage(BasePage):
    PAGE_URL = 'https://onco.zdrav.mosreg.ru/'


    BUTTON_NEWS = ("xpath","//div//h4[text()='Жизнь без риска: как двухэтапный скрининг помогает победить колоректальный рак']") 
   


    def click_button_news  (self):
        card = self.wait.until(EC.element_to_be_clickable(self.BUTTON_NEWS))
        self.driver.execute_script("arguments[0].click();", card)

