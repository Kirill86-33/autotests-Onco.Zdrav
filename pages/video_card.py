from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class VideoPage(BasePage):
    PAGE_URL = 'https://onco.zdrav.mosreg.ru/'

   
    CART_VIDEO = ("xpath", "(//div[text()='Важное'])[2]") 
    


    
    def click_button_video(self):
        element = self.wait.until(EC.element_to_be_clickable(self. CART_VIDEO))
        self.driver.execute_script("arguments[0].click();", element)