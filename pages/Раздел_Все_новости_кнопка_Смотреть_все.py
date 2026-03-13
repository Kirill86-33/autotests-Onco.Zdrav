from pages.base_page import BasePage

class ButtonSeeAll(BasePage):
    PAGE_URL = 'https://onco.zdrav.mosreg.ru/'


    BUTTON_SEE_ALL = ("xpath","(//div//a)[38]") 
                                               


    def click_button_see_all (self):  
       button_see_all = self.driver.find_element(*self.BUTTON_SEE_ALL) # Добавляем явное ожидание
       self.driver.execute_script("arguments[0].click();", button_see_all)


   