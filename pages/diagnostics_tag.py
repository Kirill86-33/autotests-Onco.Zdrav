from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class TegMedicalDiagnostics(BasePage):
    PAGE_URL = 'https://onco.zdrav.mosreg.ru/clinics'

    BLOCK_MEDICAL_DIAGNOSTICS = ("xpath", "//span[contains(text(), 'биопсия')]")  

    def click_tag(self):
        element = self.wait.until(EC.element_to_be_clickable(self.BLOCK_MEDICAL_DIAGNOSTICS))
        self.driver.execute_script("arguments[0].click();", element)