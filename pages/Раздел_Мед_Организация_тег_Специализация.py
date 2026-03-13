from pages.base_page import BasePage

class TegSpecializations(BasePage):
    PAGE_URL = 'https://onco.zdrav.mosreg.ru/clinics'


    BLOCK_SPECIALIZATION = ("xpath", "//div//span[text()='круглосуточный стационар']") 
 



    def click_button_block (self):  
        button_block = self.driver.find_element(*self.BLOCK_SPECIALIZATION) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", button_block)