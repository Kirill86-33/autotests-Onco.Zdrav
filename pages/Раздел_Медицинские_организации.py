from pages.base_page import BasePage

class MedicalOrganizations(BasePage):
    PAGE_URL = 'https://onco.zdrav.mosreg.ru/'

    CHAPTER_MEDICAL = ("xpath", "(//div//a)[29]") 
  

    def click_chapter_medical (self):  
        chapter_medical = self.driver.find_element(*self.CHAPTER_MEDICAL) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", chapter_medical)


   