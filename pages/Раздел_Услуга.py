from pages.base_page import BasePage

class ChapterService(BasePage):
    PAGE_URL = 'https://onco.zdrav.mosreg.ru/'

    CHAPTER_SERVICE = ("xpath", "(//div//a)[28]")
   
 
  
    def click_chapter_service (self):  
        chapter_service = self.driver.find_element(*self.CHAPTER_SERVICE) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", chapter_service)
