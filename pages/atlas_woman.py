from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class WomanAtlasOnco(BasePage):
    PAGE_URL = 'https://onco.zdrav.mosreg.ru/atlas'

   
    BUTTON_WOMAN = ("xpath", "//div[text()='Женщина']") 
    BUTTON_IMG = ("xpath", "(//div)[58]")



    def click_button_woman (self):
        element = self.wait.until(EC.element_to_be_clickable(self.BUTTON_WOMAN))
        self.driver.execute_script("arguments[0].click();", element)


    def click_button_img (self):
        element = self.wait.until(EC.element_to_be_clickable(self.BUTTON_IMG))
        self.driver.execute_script("arguments[0].click();", element)