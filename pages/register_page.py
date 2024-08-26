import pytest
from constants.register_page_locator import *
from pages.base_page import *

@pytest.mark.usefixtures("setup")
class Register(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        
    def hover_login_button(self):
        self.hover_over_element(LOGIN_BUTTON)
        
    def click_register_button(self):
        self.click_element(REGISTER_BUTTON)
    
    def enter_name(self,name):
        self.send_keys_input(NAME_INPUT, name)
    
    def enter_surname(self,surname):
        self.send_keys_input(SURNAME_INPUT, surname)
    
    def enter_email(self, email):
        self.send_keys_input(EMAIL_INPUT, email)
    
    def enter_password(self, password):
        self.send_keys_input(PASSWORD_INPUT, password)
        
    def click_on_agreements(self):
        self.click_element(AGREEMENTS_CHECKBOX1)
        self.click_element(AGREEMENTS_CHECKBOX2)
    
    def click_sign_up_button(self):
        self.click_element(SIGN_UP_BUTTON)
    
    def verify_code_window(self,expected_text):
        self.wait_element_visibility(VERIFY_CODE)
        location = self.find_element(VERIFY_CODE)
        actual_text = location.text
        assert actual_text == expected_text, f"Expected: '{expected_text}', Found: '{actual_text}'"
        self.take_screenshot("empty_password.png")
    
    def verify_warning_message_name(self,expected_text):
        self.wait_element_visibility(WARNING_MESSAGE_NAME)
        location = self.find_element(WARNING_MESSAGE_NAME)
        actual_text = location.text
        assert actual_text == expected_text, f"Expected: '{expected_text}', Found: '{actual_text}'"
        self.take_screenshot("warning_message_name.png")
    
    def verify_warning_message_surname(self,expected_text):
        self.wait_element_visibility(WARNING_MESSAGE_SURNAME)
        location = self.find_element(WARNING_MESSAGE_SURNAME)
        actual_text = location.text
        assert actual_text == expected_text, f"Expected: '{expected_text}', Found: '{actual_text}'"
        self.take_screenshot("warning_message_surname.png")
    
    def verify_warning_message_email(self,expected_text):
        self.wait_element_visibility(WARNING_MESSAGE_EMAIL)
        location = self.find_element(WARNING_MESSAGE_EMAIL)
        actual_text = location.text
        assert actual_text == expected_text, f"Expected: '{expected_text}', Found: '{actual_text}'"
        self.take_screenshot("warning_message_email.png")
        
    def verify_warning_message_password(self,expected_text):
        self.wait_element_visibility(WARNING_MESSAGE_PASSWORD)
        location = self.find_element(WARNING_MESSAGE_PASSWORD)
        actual_text = location.text
        assert actual_text == expected_text, f"Expected: '{expected_text}', Found: '{actual_text}'"
        self.take_screenshot("warning_message_password.png")