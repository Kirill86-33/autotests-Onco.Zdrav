from pages.base_page import BasePage

class SortByName(BasePage):
    PAGE_URL = 'https://onco.zdrav.mosreg.ru/library'

   
    BUTTON_SORT = ("xpath", "//div[text()='Сортировка:']") 
    BUTTON_BY_NAME = ("xpath", "//div[text()='По названию']") 


    def click_button_sort(self):  
        button_sort = self.driver.find_element(*self.BUTTON_SORT) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", button_sort)


    def click_button_by_name(self):  
        button_by_name = self.driver.find_element(*self.BUTTON_BY_NAME) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", button_by_name)