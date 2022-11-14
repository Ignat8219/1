import time
from selenium.webdriver import ActionChains
from pages.AuthPage import AuthPage
from selenium.webdriver.common.keys import Keys

class TestAuthPage:

    def test_auth(self, driver):
        auth_page = AuthPage(driver, 'https://b2c.passport.rt.ru')
        auth_page.open()
        auth_page.fill_fields_and_submit()

    def test_auth_phone(self, driver):
        auth_page = AuthPage(driver, 'https://b2c.passport.rt.ru')
        auth_page.open()
        auth_page.fill_fields_and_submit_phone()

    def test_photo(self, driver):
        auth_page = AuthPage(driver, 'https://b2c.passport.rt.ru')
        auth_page.open()
        time.sleep(5)
        auth_page.driver.save_screenshot('Auth_page.png')

    def test_visible_elements_of_menu (self, driver):
        auth_page = AuthPage(driver, 'https://b2c.passport.rt.ru')
        auth_page.open()
        auth_page.elements_of_menu_are_visible()

    def test_error_registration(self, driver):
        auth_page = AuthPage(driver, 'https://b2c.passport.rt.ru')
        auth_page.open()
        auth_page.fill_fields_and_submit_phone()
        time.sleep(5)
        auth_page.error_is_visible()

    def test_logo_and_slogan(self, driver):
        auth_page = AuthPage(driver, 'https://b2c.passport.rt.ru')
        auth_page.open()
        auth_page.slogan_and_logo()

    def test_cookies(self, driver):
        auth_page = AuthPage(driver, 'https://b2c.passport.rt.ru')
        auth_page.open()
        auth_page.cookies()

    def test_chat(self,driver):
        auth_page = AuthPage(driver, 'https://b2c.passport.rt.ru')
        auth_page.open()
        time.sleep(5)
        auth_page.chat()

    def test_network_btns(self,driver):
        auth_page = AuthPage(driver, 'https://b2c.passport.rt.ru')
        auth_page.open()
        auth_page.link_network_vk()
        driver.back()
        auth_page.link_network_ok()
        driver.back()
        auth_page.link_network_mail()
        driver.back()
        auth_page.link_network_google()
        driver.back()
        auth_page.link_network_ya()
        driver.back()

    def test_conf_and_supp(self,driver):
        auth_page = AuthPage(driver, 'https://b2c.passport.rt.ru')
        auth_page.open()
        auth_page.link_conf()
        ActionChains(driver).key_down(Keys.CONTROL).send_keys("t").key_up(Keys.CONTROL).perform()
        auth_page.link_supp()
        ActionChains(driver).key_down(Keys.CONTROL).send_keys("t").key_up(Keys.CONTROL).perform()

    def test_forgot_password(self,driver):
        auth_page = AuthPage(driver, 'https://b2c.passport.rt.ru')
        auth_page.open()
        auth_page.forgot_password()









