from pages.base_page import BasePage

class ButtonLpu(BasePage):
    PAGE_URL = 'https://onco.zdrav.mosreg.ru/clinics'

    BUTTON_LPU = ("xpath", "(//div//a)[11]")
  
 
  


    def click_button_lpu (self):  
        button_lpu = self.driver.find_element(*self.BUTTON_LPU) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", button_lpu)


