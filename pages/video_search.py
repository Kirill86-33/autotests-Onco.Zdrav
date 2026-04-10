from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


class VideoSearchPage(BasePage):
    PAGE_URL = 'https://onco.zdrav.mosreg.ru/library'

    BUTTON_SEARCH = ("xpath", "//div//input[@placeholder='Поиск']") 
    SECTION_VIDEO = ("xpath", "//div//h5[text()='Вопросы для онколога: какие рекомендации следует соблюдать во время лечения?']")

   
    def enter_input_search  (self, text):
        field = self.wait.until(EC.visibility_of_element_located(self.BUTTON_SEARCH))
        field.clear()
        field.send_keys(text)
        field.send_keys(Keys.ENTER)   
        time.sleep(1)  



    def click_button_section_video (self):
        card = self.wait.until(EC.element_to_be_clickable(self.SECTION_VIDEO))
        self.driver.execute_script("arguments[0].click();", card)