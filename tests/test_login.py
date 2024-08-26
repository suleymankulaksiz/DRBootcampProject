import pytest
from pages.login_page import *

@pytest.mark.usefixtures("setup")
class TestLogin:
    
    def test_successful_login(self):
        login = Login(self.driver)
        login.hover_login_button()
        login.click_login_button()
        login.accept_cookies()
        login.enter_email("denemehesabi299@outlook.com")
        login.enter_password("denemeQA159753")
        login.click_captcha()
        login.click_login_form()
        login.verify_successful_login("Hesabım")
    
    def test_correct_email_wrong_password(self):
        login = Login(self.driver)
        login.hover_login_button()
        login.click_login_button()
        login.accept_cookies()
        login.enter_email("denemehesabi299@outlook.com")
        login.enter_password("1234567QA")
        login.click_captcha()
        login.click_login_form()
        login.verify_correct_password_wrong_email("Hatalı e-posta adresi ya da şifre girdiniz.")
        
    def test_wrong_email_correct_password(self):
        login = Login(self.driver)
        login.hover_login_button()
        login.click_login_button()
        login.accept_cookies()
        login.enter_email("deneme123@gmail.com")
        login.enter_password("denemeQA159753")
        login.click_captcha()
        login.click_login_form()
        login.verify_wrong_email_correct_password("Hatalı e-posta adresi ya da şifre girdiniz.")
        
    def test_empty_email(self):
        login = Login(self.driver)
        login.hover_login_button()
        login.click_login_button()
        login.accept_cookies()
        login.enter_email("")
        login.enter_password("denemeQA159753")
        login.click_captcha()
        login.click_login_form()
        login.verify_empty_email("Lütfen e-posta adresinizi giriniz.")
    
    def test_empty_password(self):
        login = Login(self.driver)
        login.hover_login_button()
        login.click_login_button()
        login.accept_cookies()
        login.enter_email("denemehesabi299@outlook.com")
        login.enter_password("")
        login.click_captcha()
        login.click_login_form()
        login.verify_empty_password("Lütfen şifrenizi giriniz.")