from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class QuestionAnswer(BasePage):
    PAGE_URL = 'https://onco.zdrav.mosreg.ru/faq'
    
    INPUT_NAME = ("xpath", "//input[@id='name']")  
    INPUT_PHONE = ("xpath", "//input[@id='phone']")
    INPUT_EMAIL = ("xpath", "//input[@id='email']")
    INPUT_DISTRICT = ("xpath", "//input[@id='district']")
    INPUT_COMMENT = ("xpath", "//div//textarea[@id='comment']")
    BUTTON_SEND = ("xpath", "//button[text()='Отправить']")

    
    
    def enter_name (self, name):  
        input_name = self.wait.until(EC.visibility_of_element_located(self.INPUT_NAME))
        input_name.send_keys(name)


    def enter_phone (self, phone):  
        input_name = self.wait.until(EC.visibility_of_element_located(self.INPUT_PHONE))
        input_name.send_keys(phone)


    def enter_email (self, email):  
        input_name = self.wait.until(EC.visibility_of_element_located(self.INPUT_EMAIL))
        input_name.send_keys(email)


    def enter_district (self, district):  
        input_name = self.wait.until(EC.visibility_of_element_located(self.INPUT_DISTRICT))
        input_name.send_keys(district)


    def enter_comment (self, comment):    
        input_name = self.wait.until(EC.visibility_of_element_located(self.INPUT_COMMENT))
        input_name.send_keys(comment)



    def click_send_button(self):
        button = self.driver.find_element(*self.BUTTON_SEND)
        self.driver.execute_script("arguments[0].click();", button)