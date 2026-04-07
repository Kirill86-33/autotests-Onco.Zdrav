from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver

class BasePage:
    LOGO = ("xpath", "//div[@class='MuiBox-root css-matur']") 

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(driver, 10)



    def open(self):
        if hasattr(self, 'PAGE_URL'):
            self.driver.get(self.PAGE_URL)
            self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
          

          

    def logo(self):
        # Используем self.wait вместо find_element
        logo_element = self.wait.until(EC.element_to_be_clickable(self.LOGO))
        logo_element.click()



 