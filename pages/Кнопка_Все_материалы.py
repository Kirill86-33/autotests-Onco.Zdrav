from pages.base_page import BasePage

class AllMaterials(BasePage):
    PAGE_URL = 'https://onco.zdrav.mosreg.ru/'

   
    BUTTON_ALL_MATERIALS = ("xpath", "(//div//a)[33]") 
    


    def click_button_all_materials(self):  
        button_materials = self.driver.find_element(*self.BUTTON_ALL_MATERIALS) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", button_materials)
