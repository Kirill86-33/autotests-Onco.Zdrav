from pages.base_page import BasePage

class TegTopic(BasePage):
    PAGE_URL = 'https://onco.zdrav.mosreg.ru/library'


    BLOCK_TOPIC = ("xpath", "(//div)[71]") 
    BUTTON_VIDEO = ("xpath", "(//div//h5)[1]")



    def click_button_block_topic (self):  
        button_topic = self.driver.find_element(*self.BLOCK_TOPIC) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", button_topic)


    def click_button_video(self):  
        button_video = self.driver.find_element(*self.BUTTON_VIDEO) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", button_video)