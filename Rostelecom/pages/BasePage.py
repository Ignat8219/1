from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as Wait

class BasePage:

    def __init__(self, driver, url):
        self.url = url
        self.driver = driver
        self.timeout = 30
        self.find_element = driver.find_element

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator,timeout=5):
        return Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))



