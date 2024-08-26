import pytest
from pages.register_page import *
from constants.register_page_locator import *

@pytest.mark.usefixtures("setup")
class TestRegister:
    
    def test_successful_register(self):
        email_random =generate_random_email()
        register = Register(self.driver)
        register.hover_login_button()
        register.click_register_button()
        register.accept_cookies()
        register.enter_name("Techcareer")
        register.enter_surname("QA")
        register.enter_email(email_random)
        register.enter_password("denemeQA159753")
        register.click_on_agreements()
        register.click_sign_up_button()
        register.verify_code_window("Doğrulama Kodunu Girin")
    
    def test_empty_name(self):
        email_random =generate_random_email()
        register = Register(self.driver)
        register.hover_login_button()
        register.click_register_button()
        register.accept_cookies()
        register.enter_name("")
        register.enter_surname("QA")
        register.enter_email(email_random)
        register.enter_password("denemeQA159753")
        register.click_on_agreements()
        register.click_sign_up_button()
        register.verify_warning_message_name("Lütfen adınızı giriniz.")
        
    def test_empty_surname(self):
        email_random =generate_random_email()
        register = Register(self.driver)
        register.hover_login_button()
        register.click_register_button()
        register.accept_cookies()
        register.enter_name("Techcareer")
        register.enter_surname("")
        register.enter_email(email_random)
        register.enter_password("denemeQA159753")
        register.click_on_agreements()
        register.click_sign_up_button()
        register.verify_warning_message_surname("Lütfen soyadınızı giriniz.")
        
    def test_empty_email(self):
        email_random =generate_random_email()
        register = Register(self.driver)
        register.hover_login_button()
        register.click_register_button()
        register.accept_cookies()
        register.enter_name("Techcareer")
        register.enter_surname("QA")
        register.enter_email("")
        register.enter_password("denemeQA159753")
        register.click_on_agreements()
        register.click_sign_up_button()
        register.verify_warning_message_email("Lütfen e-posta adresinizi giriniz.")
        
    def test_empty_password(self):
        email_random =generate_random_email()
        register = Register(self.driver)
        register.hover_login_button()
        register.click_register_button()
        register.accept_cookies()
        register.enter_name("Techcareer")
        register.enter_surname("QA")
        register.enter_email(email_random)
        register.enter_password("")
        register.click_on_agreements()
        register.click_sign_up_button()
        register.verify_warning_message_password("Lütfen şifrenizi giriniz.")