from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
class TegTopic(BasePage):
    PAGE_URL = 'https://onco.zdrav.mosreg.ru/library'


    BLOCK_TOPIC = ("xpath", "//div//span[text()='Головной мозг']") 
    BUTTON_VIDEO = ("xpath", "//div//h5[text()='Врачи областного онкодиспансера удаляют опухоли под микроскопом']")


    def wait_for_page_load(self):
        self.wait.until(EC.visibility_of_element_located(self.BLOCK_TOPIC))



    def click_button_block_topic(self):
        self.wait_for_page_load()
        element = self.wait.until(EC.element_to_be_clickable(self.BLOCK_TOPIC))
        self.driver.execute_script("arguments[0].click();", element)



    def click_button_video(self):
        element = self.wait.until(EC.element_to_be_clickable(self.BUTTON_VIDEO))
        self.driver.execute_script("arguments[0].click();", element)