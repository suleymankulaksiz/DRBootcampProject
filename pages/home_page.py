import pytest
from constants.login_page_locator import *
from pages.base_page import *

@pytest.mark.usefixtures("setup")
class HomePage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        
    def verify_homepage_opened(self,assert_url):
        self.take_screenshot("verify_homepage_opened.png")
        assert assert_url == self.driver.current_url, f"Expected '{assert_url}' to be in '{self.driver.current_url}'"
    
    def hover_electronic_catalog(self):
        self.hover_over_element(ELECTRONIC_CATALOG_HOVER)
    
    def click_sub_categories(self):
        self.click_element(SUBCATEGORY)
    
    def verify_sub_categories_opened(self, expected_text):
        self.take_screenshot("verify_sub_categories_opened.png")
        location = self.find_element(SUBCATEGORY_TEXT)
        actual_text = location.text
        assert actual_text == expected_text, f"Expected: '{expected_text}', Found: '{actual_text}'"
    
    def click_first_product(self):
        self.click_element(FIRST_PRODUCT)
    
    def verify_first_product_page_opened(self,expected_text):
        self.take_screenshot("verify_first_product_page_opened.png")
        location = self.find_element(FIRST_PRODUCT_PAGE_CONTROL)
        actual_text = location.text
        assert actual_text == expected_text, f"Expected: '{expected_text}', Found: '{actual_text}'"
    
    def add_product_to_cart_button(self):
        self.click_element(ADD_TO_CART_BUTTON)
    
    def verify_add_product_to_cart_item_control(self,expected_text):
        time.sleep(1)
        location = self.find_element(ADD_TO_CART_ITEM_CONTROL)
        actual_text = location.text
        assert actual_text == expected_text, f"Expected: '{expected_text}', Found: '{actual_text}'"
        self.take_screenshot("verify_add_product_to_cart_item_control.png")
    
    def click_on_the_go_to_cart_button(self):
        self.click_element(GO_TO_CART_BUTTON)