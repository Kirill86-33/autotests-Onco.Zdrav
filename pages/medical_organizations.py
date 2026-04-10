from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class MedicalOrganizations(BasePage):
    PAGE_URL = 'https://onco.zdrav.mosreg.ru/'

   
    CHAPTER_MEDICAL = ("xpath", "//*[@id='__next']/main/div/div[2]/div[1]/div[3]/div[2]/a/h4")
    CART_LPU = ("xpath", "//h4[contains(text(), 'Видновская клиническая больница')]")



    def click_chapter_medical(self):
        element = self.wait.until(EC.presence_of_element_located(self.CHAPTER_MEDICAL))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        clickable = self.wait.until(EC.element_to_be_clickable(self.CHAPTER_MEDICAL))
        self.driver.execute_script("arguments[0].click();", clickable)



    def click_cart_lpu(self):
        element = self.wait.until(EC.element_to_be_clickable(self.CART_LPU))
        self.driver.execute_script("arguments[0].click();", element)