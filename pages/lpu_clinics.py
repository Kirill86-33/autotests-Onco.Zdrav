from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
class ButtonLpu(BasePage):
    PAGE_URL = 'https://onco.zdrav.mosreg.ru/clinics'

    BUTTON_LPU = ("xpath", "//div//h4[text()='ГБУЗ Московской области «Волоколамская больница»']")
  
 

    def click_button_lpu (self):
        card = self.wait.until(EC.element_to_be_clickable(self.BUTTON_LPU))
        self.driver.execute_script("arguments[0].click();", card)