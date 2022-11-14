import time
from pages.BasePage import BasePage
from locators.Locators import RegLocators as Locators

class RegPage(BasePage):

    def reg_link(self):
        self.element_is_visible(Locators.AUTH_LINK_REG).click()

    def correct_completion(self):
        FIRSTNAME = 'Иван'
        LASTNAME = 'Иванов'
        REGION = 'Москва'
        EMAIL = 'ignat-@mail.ru'
        PASSWORD = 'Welcome1!123'
        self.element_is_visible(Locators.REG_FIRST_NAME).send_keys(FIRSTNAME)
        self.element_is_visible(Locators.REG_LAST_NAME).send_keys(LASTNAME)
        self.element_is_visible(Locators.REG_REG).send_keys(REGION)
        self.element_is_visible(Locators.REG_EMAIL_OR_NUMBER).send_keys(EMAIL)
        self.element_is_visible(Locators.REG_PASS).send_keys(PASSWORD)
        self.element_is_visible(Locators.REG_PASS_CON).send_keys(PASSWORD)
        self.element_is_visible(Locators.REG_BTN).click()
        time.sleep(5)

    def incorrec_completion(self):
        FIRSTNAME = 'Qw'
        LASTNAME = 'Qw'
        REGION = 'Moscow'
        EMAIL = 'qw'
        PASSWORD = 'qw'
        self.element_is_visible(Locators.REG_FIRST_NAME).send_keys(FIRSTNAME)
        self.element_is_visible(Locators.REG_LAST_NAME).send_keys(LASTNAME)
        self.element_is_visible(Locators.REG_REG).send_keys(REGION)
        self.element_is_visible(Locators.REG_EMAIL_OR_NUMBER).send_keys(EMAIL)
        self.element_is_visible(Locators.REG_PASS).send_keys(PASSWORD)
        self.element_is_visible(Locators.REG_PASS_CON).send_keys(PASSWORD)
        self.element_is_visible(Locators.REG_BTN).click()
        time.sleep(5)

    def system_comments_incor_comp(self):
        self.element_is_visible(Locators.REG_INC_FN_COMP)
        self.element_is_visible(Locators.REG_INC_LN_COMP)
        self.element_is_visible(Locators.REG_INK_EMAIL_COMP)
        self.element_is_visible(Locators.REG_INK_PAS_COMP)
        self.element_is_visible(Locators.REG_INK_CONF_PAS_COMP)
        time.sleep(5)

    def logo (self):
        self.element_is_visible(Locators.REG_LOGO)


    def cookies(self):
        self.element_is_visible(Locators.REG_LINK_COOKIE).click()
        self.element_is_visible(Locators.REG_COOKIE_INFORMATION)

    def link_conf(self):
        self.element_is_visible(Locators.REG_LINK_CP).click()
    def link_supp(self):
        self.element_is_visible(Locators.REG_LINK_UA2).click()

    def acc_is_exi (self):
        self.element_is_visible(Locators.REG_ACC_EXI)

