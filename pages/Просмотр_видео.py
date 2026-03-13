from pages.base_page import BasePage

class VideoPage(BasePage):
    PAGE_URL = 'https://onco.zdrav.mosreg.ru/'

   
    BUTTON_VIDEO = ("xpath", "(//div//a)[35]") 
    


    def click_button_video(self):  
        button_video = self.driver.find_element(*self.BUTTON_VIDEO) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", button_video)


    
   