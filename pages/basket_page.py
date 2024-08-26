import pytest
from constants.basket_page_locator import *
from pages.base_page import *
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setup")
class Basket(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    def verify_basket_page_opened(self,expected_text):
        location = self.find_element(BASKET_PAGE_TEXT)
        actual_text = location.text
        assert actual_text == expected_text, f"Expected: '{expected_text}', Found: '{actual_text}'"
        self.take_screenshot("verify_basket_page_opened.png")
        