from selenium.webdriver.common.by import By


class AuthLocators:
    AUTH_LINK = 'https://b2c.passport.rt.ru'
    AUTH_LOGO_LOCATOR1 = (By.CSS_SELECTOR, 'svg[class*="rt-logo main-header__logo"]')
    AUTH_LOGO_LOCATOR2 = (By.CSS_SELECTOR, 'svg[class*="rt-logo what-is-container__logo"]')
    AUTH_EMAIL_LINK = (By.CSS_SELECTOR, '#t-btn-tab-mail')
    AUTH_EMAIL = (By.CSS_SELECTOR, '#username')
    AUTH_PASS = (By.CSS_SELECTOR, '#password')
    AUTH_BTN = (By.CSS_SELECTOR, '#kc-login')
    AUTH_LINK_UA1 = (By.CSS_SELECTOR, 'a[class*=rt-link--orange]')
    AUTH_LINK_VK = (By.CSS_SELECTOR, '#oidc_vk')
    AUTH_LINK_OK = (By.CSS_SELECTOR, '#oidc_ok')
    AUTH_LINK_MAIL = (By.CSS_SELECTOR, '#oidc_mail')
    AUTH_LINK_GOOGLE = (By.CSS_SELECTOR, '#oidc_google')
    AUTH_LINK_YA = (By.CSS_SELECTOR, '#oidc_ya')
    AUTH_LINK_COOKIE = (By.CSS_SELECTOR, 'span[class*="rt-footer-left__item-accent"]')
    AUTH_LINK_CP = (By.XPATH, '//*[@id="rt-footer-agreement-link"]/span[1]')
    AUTH_LINK_UA2 = (By.XPATH, '//*[@id="rt-footer-agreement-link"]/span[2]')
    AUTH_LINK_PHONE = (By.CSS_SELECTOR, 'a[class="rt-footer-right__support-phone"]')
    AUTH_REG_PHONE = (By.CSS_SELECTOR, '#t-btn-tab-phone')
    AUTH_REG_EMAIL = (By.CSS_SELECTOR, '#t-btn-tab-mail')
    AUTH_REG_LOGIN = (By.CSS_SELECTOR, '#t-btn-tab-login')
    AUTH_REG_PER_ACC = (By.CSS_SELECTOR, '#t-btn-tab-ls')
    AUTH_REG_ERROR = (By.CSS_SELECTOR, 'p[class*="card-container__error"]')
    AUTH_SLOGAN = (By.CSS_SELECTOR, 'p[class*="what-is__desc"]')
    AUTH_COOKIE_INFORMATION = (By.CSS_SELECTOR, 'div[class*="rt-cookies-tip__desc-container"]')
    AUTH_TELEGRAM = (By.CSS_SELECTOR, 'div[class*="icon telegram svelte-16eyo30"]')
    AUTH_VIBER = (By.CSS_SELECTOR, 'div[class*="icon viber svelte-16eyo30"]')
    AUTH_CHAT = (By.CSS_SELECTOR, 'div[class*="omnichat-text"]')
    AUTH_CHAT_NAME = (By.CSS_SELECTOR, '#full-name')
    AUTH_CHAT_PHONE = (By.CSS_SELECTOR, '#phone')
    AUTH_CHAT_BTN = (By.CSS_SELECTOR, '#widget_sendPrechat')
    AUTH_FORG_PASS = (By.CSS_SELECTOR, '#forgot_password')





class RegLocators:
    AUTH_LINK_REG = (By.CSS_SELECTOR, '#kc-register')
    REG_FIRST_NAME = (By.NAME, 'firstName')
    REG_LAST_NAME = (By.NAME, 'lastName')
    REG_REG = (By.CSS_SELECTOR, 'input[autocomplete*="new-password"]')
    REG_EMAIL_OR_NUMBER = (By.CSS_SELECTOR, '#address')
    REG_PASS = (By.CSS_SELECTOR, '#password')
    REG_PASS_CON = (By.CSS_SELECTOR, '#password-confirm')
    REG_BTN = (By.NAME, 'register')
    REG_LINK_UA1 = (By.CSS_SELECTOR, 'a[class*=rt-link--orange]')
    REG_LINK_COOKIE = (By.XPATH, '//*[@id="app-footer"]/div[1]/div[2]/span/span')
    REG_LINK_CP = (By.XPATH, '//*[@id="rt-footer-agreement-link"]/span[1]')
    REG_LINK_UA2 = (By.XPATH, '//*[@id="rt-footer-agreement-link"]/span[2]')
    REG_LINK_PHONE = (By.CSS_SELECTOR, 'a[class="rt-footer-right__support-phone"]')
    REG_INC_FN_COMP = (By.CSS_SELECTOR, 'span[class*="rt-input-container__meta--error"]')
    REG_INC_LN_COMP = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span')
    REG_INK_EMAIL_COMP = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[3]/span')
    REG_INK_PAS_COMP = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span')
    REG_INK_CONF_PAS_COMP = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span')
    REG_LOGO = (By.CSS_SELECTOR, 'svg[class*="main-header__logo"]')
    REG_COOKIE_INFORMATION = (By.CSS_SELECTOR, 'div[class*="rt-cookies-tip__desc-container"]')
    REG_ACC_EXI = (By.CSS_SELECTOR, 'h2[class*="card-modal__title"]')




class AccPage:
    ACC_LOGO = (By.CSS_SELECTOR, 'h3[class*="card-title"]')