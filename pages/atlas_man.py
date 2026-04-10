from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC



class ChapterAtlasOnco(BasePage):
    PAGE_URL = 'https://onco.zdrav.mosreg.ru/atlas'

    CHAPTER_ATTLAS_ONCO = ("xpath", "(//div)[58]")
    BUTTON_VISION_HEARING = ("xpath", "//div[text()='Рак головного мозга']")
 



    def click_chapter_onco_atlas (self):
        element = self.wait.until(EC.element_to_be_clickable(self.CHAPTER_ATTLAS_ONCO))
        self.driver.execute_script("arguments[0].click();", element)


    def click_vision_hearing (self):
        element = self.wait.until(EC.element_to_be_clickable(self.BUTTON_VISION_HEARING))
        self.driver.execute_script("arguments[0].click();", element)



