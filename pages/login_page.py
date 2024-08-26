from time import sleep
import pytest
from constants.login_page_locator import *
from pages.base_page import *

@pytest.mark.usefixtures("setup")
class Login(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        
    def hover_login_button(self):
        self.hover_over_element(LOGIN_BUTTON_HOVER)
        
    def click_login_button(self):
        self.click_element(LOGIN_BUTTON)
    
    def enter_email(self, username):
        self.send_keys_input(INPUT_EMAIL, username)
    
    def enter_password(self, password):
        self.send_keys_input(INPUT_PASSWORD, password)
    
    def click_captcha(self):
        iframe = self.find_element(IFRAME_XPATH)
        self.driver.switch_to.frame(iframe)
        captcha = self.find_element(CAPTCHA_XPATH)
        captcha.click()
        sleep(10) #Eğer görsel doğrulama isterse.
    
    def click_login_form(self):
        self.switch_to_window(0)
        self.click_element(LOGIN_BUTTON_FORM)
    
    def verify_successful_login(self,expected_text):
        self.wait_element_visibility(SUCCESSFUL_LOGIN_MESSAGE)
        location = self.find_element(SUCCESSFUL_LOGIN_MESSAGE)
        actual_text = location.text
        assert actual_text == expected_text, f"Expected: '{expected_text}', Found: '{actual_text}'"
        self.take_screenshot("successful_login.png")
        
    def verify_correct_password_wrong_email(self, expected_text):
        self.wait_element_visibility(INCORRECT_EMAIL_MESSAGE)
        location = self.find_element(INCORRECT_EMAIL_MESSAGE)
        actual_text = location.text
        assert actual_text == expected_text, f"Expected: '{expected_text}', Found: '{actual_text}'"
        self.take_screenshot("correct_password_wrong_email.png")
    
    def verify_wrong_email_correct_password(self, expected_text):
        self.wait_element_visibility(INCORRECT_PASSWORD_MESSAGE)
        location = self.find_element(INCORRECT_PASSWORD_MESSAGE)
        actual_text = location.text
        assert actual_text == expected_text, f"Expected: '{expected_text}', Found: '{actual_text}'"
        self.take_screenshot("wrong_email_correct_password.png")
    
    def verify_empty_email(self, expected_text):
        self.wait_element_visibility(EMPTY_EMAIL_MESSAGE)
        location = self.find_element(EMPTY_EMAIL_MESSAGE)
        actual_text = location.text
        assert actual_text == expected_text, f"Expected: '{expected_text}', Found: '{actual_text}'"
        self.take_screenshot("empty_email.png")
    
    def verify_empty_password(self, expected_text):
        self.wait_element_visibility(EMPTY_PASSWORD_MESSAGE)
        location = self.find_element(EMPTY_PASSWORD_MESSAGE)
        actual_text = location.text
        assert actual_text == expected_text, f"Expected: '{expected_text}', Found: '{actual_text}'"
        self.take_screenshot("empty_password.png")