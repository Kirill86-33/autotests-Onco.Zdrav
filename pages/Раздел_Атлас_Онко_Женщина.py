from pages.base_page import BasePage

class WomanAtlasOnco(BasePage):
    PAGE_URL = 'https://onco.zdrav.mosreg.ru/atlas'

   
    BUTTON_WOMAN = ("xpath", "//div[text()='Женщина']") 
    BUTTON_IMG = ("xpath", "(//div)[58]")


    def click_button_woman(self):  
        button_woman = self.driver.find_element(*self.BUTTON_WOMAN) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", button_woman)


    
    def click_button_img(self):  
        button_img = self.driver.find_element(*self.BUTTON_IMG) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", button_img)