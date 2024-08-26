import string
from selenium.webdriver.common.by import By
import random

def generate_random_email():
        # Rastgele bir e-posta adresi oluştur
        username = ''.join(random.choice(string.ascii_letters) for _ in range(8))
        domain = random.choice(['gmail', 'hotmail', 'outlook', 'yahoo', 'yandex'])

        extension = random.choice(['com', 'net', 'org'])

        extension = random.choice(['com', 'net', 'org'])                                       #burada random mail oluşturma işlemi yapıyoruz.

    
        emailrandom = f"{username}@{domain}.{extension}"
        return emailrandom


LOGIN_BUTTON =(By.CSS_SELECTOR, "[class='info-menu col-4 d-none d-lg-flex dr-flex-end'] div:nth-child(3) .font-weight-bold")
REGISTER_BUTTON =(By.LINK_TEXT, "Üye Ol")
NAME_INPUT = (By.ID,"firstName")
SURNAME_INPUT = (By.ID,"lastName")
EMAIL_INPUT = (By.ID,"email")
PASSWORD_INPUT = (By.ID,"passwordNew")
AGREEMENTS_CHECKBOX1 = (By.CSS_SELECTOR,"div:nth-of-type(7) > .control.control-checkbox.pt-6.register__form-check-label > .check_v2")
AGREEMENTS_CHECKBOX2 = (By.CSS_SELECTOR,"div:nth-of-type(8) > .control.control-checkbox.pt-6.register__form-check-label > .check_v2")
SIGN_UP_BUTTON = (By.CSS_SELECTOR,".bg-c1.button.fs-4.my-5.py-10.text-c255.text-center")
VERIFY_CODE = (By.CSS_SELECTOR,"[class='gsm-validation__title']")
WARNING_MESSAGE_NAME = (By.ID,"firstName-error")
WARNING_MESSAGE_SURNAME = (By.ID,"lastName-error")
WARNING_MESSAGE_EMAIL =(By.ID,"email-error")
WARNING_MESSAGE_PASSWORD=(By.ID,"passwordNew-error")