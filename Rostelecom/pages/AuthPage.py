import time
from pages.BasePage import BasePage
from locators.Locators import AuthLocators as Locators



class AuthPage(BasePage):

    def fill_fields_and_submit(self):
        email = 'ignat-@mail.ru'
        password = 'Welcome1!123'
        self.element_is_visible(Locators.AUTH_EMAIL_LINK).click()
        self.element_is_visible(Locators.AUTH_EMAIL).send_keys(email)
        self.element_is_visible(Locators.AUTH_PASS).send_keys(password)
        self.element_is_visible(Locators.AUTH_BTN).click()
        time.sleep(5)

    def elements_of_menu_are_visible(self):
        self.element_is_visible(Locators.AUTH_REG_PHONE)
        self.element_is_visible(Locators.AUTH_REG_EMAIL)
        self.element_is_visible(Locators.AUTH_REG_LOGIN)
        self.element_is_visible(Locators.AUTH_REG_PER_ACC)

    def error_is_visible(self):
        self.element_is_visible(Locators.AUTH_REG_ERROR)

    def fill_fields_and_submit_phone(self):
        phone = 89111111111
        password = 'Welcome1!123'
        self.element_is_visible(Locators.AUTH_REG_PHONE).click()
        self.element_is_visible(Locators.AUTH_EMAIL).send_keys(phone)
        self.element_is_visible(Locators.AUTH_PASS).send_keys(password)
        self.element_is_visible(Locators.AUTH_BTN).click()
        time.sleep(5)

    def slogan_and_logo (self):
        self.element_is_visible(Locators.AUTH_LOGO_LOCATOR1)
        self.element_is_visible(Locators.AUTH_LOGO_LOCATOR2)
        self.element_is_visible(Locators.AUTH_SLOGAN)

    def cookies(self):
        self.element_is_visible(Locators.AUTH_LINK_COOKIE).click()
        self.element_is_visible(Locators.AUTH_COOKIE_INFORMATION)

    def chat(self):
        phone = 89111111111
        name = 'Иван'
        self.element_is_visible(Locators.AUTH_CHAT).click()
        self.element_is_visible(Locators.AUTH_CHAT_NAME).send_keys(name)
        self.element_is_visible(Locators.AUTH_CHAT_PHONE).send_keys(phone)
        self.element_is_visible(Locators.AUTH_CHAT_BTN).click()

    def link_network_vk(self):
        self.element_is_visible(Locators.AUTH_LINK_VK).click()
    def link_network_ok(self):
        self.element_is_visible(Locators.AUTH_LINK_OK).click()
    def link_network_mail(self):
        self.element_is_visible(Locators.AUTH_LINK_MAIL).click()
    def link_network_google(self):
        self.element_is_visible(Locators.AUTH_LINK_GOOGLE).click()
    def link_network_ya(self):
        self.element_is_visible(Locators.AUTH_LINK_YA).click()

    def link_conf(self):
        self.element_is_visible(Locators.AUTH_LINK_CP).click()
    def link_supp(self):
        self.element_is_visible(Locators.AUTH_LINK_CP).click()

    def reg_link(self):
        self.element_is_visible(Locators.AUTH_LINK_REG).click()

    def forgot_password(self):
        email = 'ignat-@mail.ru'
        self.element_is_visible(Locators.AUTH_FORG_PASS).click()
        self.element_is_visible(Locators.AUTH_EMAIL).send_keys(email)
        time.sleep(20)


















