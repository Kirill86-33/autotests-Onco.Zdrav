from pages.base_page import BasePage

class TegMedicalDiagnostics(BasePage):
    PAGE_URL = 'https://onco.zdrav.mosreg.ru/clinics'


    BLOCK_MEDICAL_DIAGNOSTICS = ("xpath", "//div//span[text()='биопсия']") 
 



    def click_button_block_diagnostics (self):  
        button_diagnostics = self.driver.find_element(*self.BLOCK_MEDICAL_DIAGNOSTICS) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", button_diagnostics)