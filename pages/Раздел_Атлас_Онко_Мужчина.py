from pages.base_page import BasePage

class ChapterAtlasOnco(BasePage):
    PAGE_URL = 'https://onco.zdrav.mosreg.ru/'

    CHAPTER_ATTLAS_ONCO = ("xpath", "(//div//a)[35]")
    BUTTON_VISION_HEARING = ("xpath", "(//div[@class='css-1066xne'])[1]")
    BUTTON_EYE_TUMOR = ("xpath", "//div[text()='Злокачественные опухоли глаз']")



    def click_chapter_onco_atlas (self):  
        chapter_onco_atlas = self.driver.find_element(*self.CHAPTER_ATTLAS_ONCO) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", chapter_onco_atlas)


  
    def click_vision_hearing(self):  
        chapter_vision = self.driver.find_element(*self.BUTTON_VISION_HEARING) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", chapter_vision)


    def click_eye_tumor (self):  
        chapter_eye = self.driver.find_element(*self.BUTTON_EYE_TUMOR) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", chapter_eye)