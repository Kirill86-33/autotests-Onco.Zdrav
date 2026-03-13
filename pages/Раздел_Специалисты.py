from pages.base_page import BasePage

class Specialists(BasePage):
    PAGE_URL = 'https://onco.zdrav.mosreg.ru/'

    CHAPTER_SPECIALISTS = ("xpath", "(//div//a)[34]") 
  

    def click_chapter_specialists(self):  
        chapter_specialists = self.driver.find_element(*self.CHAPTER_SPECIALISTS) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", chapter_specialists)
