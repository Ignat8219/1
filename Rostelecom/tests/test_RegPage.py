from selenium.webdriver import ActionChains
from pages.RegPage import RegPage


from selenium.webdriver.common.keys import Keys

class TestRegPage:

    def test_completion_reg_form(self, driver):
        reg_page = RegPage(driver, 'https://b2c.passport.rt.ru')
        reg_page.open()
        reg_page.reg_link()
        reg_page.correct_completion()

    def test_acc_is_exi(self, driver):
        reg_page = RegPage(driver, 'https://b2c.passport.rt.ru')
        reg_page.open()
        reg_page.reg_link()
        reg_page.correct_completion()
        reg_page.acc_is_exi()

    def test_completion_reg_form_incorr(self, driver):
        reg_page = RegPage(driver, 'https://b2c.passport.rt.ru')
        reg_page.open()
        reg_page.reg_link()
        reg_page.incorrec_completion()
        reg_page.system_comments_incor_comp()

    def test_logo(self, driver):
        reg_page = RegPage(driver, 'https://b2c.passport.rt.ru')
        reg_page.open()
        reg_page.reg_link()
        reg_page.logo()

    def test_cookies(self, driver):
        reg_page = RegPage(driver, 'https://b2c.passport.rt.ru')
        reg_page.open()
        reg_page.reg_link()
        reg_page.cookies()

    def test_conf_and_supp(self,driver):
        reg_page = RegPage(driver, 'https://b2c.passport.rt.ru')
        reg_page.open()
        reg_page.reg_link()
        reg_page.link_conf()
        ActionChains(driver).key_down(Keys.CONTROL).send_keys("t").key_up(Keys.CONTROL).perform()
        reg_page.link_supp()
        ActionChains(driver).key_down(Keys.CONTROL).send_keys("t").key_up(Keys.CONTROL).perform()

