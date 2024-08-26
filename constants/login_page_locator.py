from selenium.webdriver.common.by import By

LOGIN_BUTTON_HOVER =(By.CSS_SELECTOR, "[class='info-menu col-4 d-none d-lg-flex dr-flex-end'] div:nth-child(3) .font-weight-bold")
LOGIN_BUTTON =(By.LINK_TEXT, "Giriş Yap")
INPUT_EMAIL = (By.ID,"email")
INPUT_PASSWORD = (By.ID,"password")
IFRAME_XPATH= (By.XPATH,"//iframe[@title='reCAPTCHA']")
CAPTCHA_XPATH = (By.XPATH,"//*[@id='recaptcha-anchor']")
LOGIN_BUTTON_FORM = (By.CSS_SELECTOR,".login__form [data-tab='email'] [value='Giriş Yap']")

SUCCESSFUL_LOGIN_MESSAGE = (By.CSS_SELECTOR,"[class='info-menu col-4 d-none d-lg-flex dr-flex-end'] div:nth-child(3) .font-weight-bold")
INCORRECT_EMAIL_MESSAGE = (By.CSS_SELECTOR,".login__form-error-message .js-login-error-text")
INCORRECT_PASSWORD_MESSAGE =(By.CSS_SELECTOR,".login__form-error-message .js-login-error-text")
EMPTY_EMAIL_MESSAGE = (By.ID,"email-error")
EMPTY_PASSWORD_MESSAGE =(By.ID,"password-error")