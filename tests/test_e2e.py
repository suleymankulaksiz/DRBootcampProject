import pytest
from pages.login_page import *
from pages.home_page import *
from pages.basket_page import *
import allure

@pytest.mark.usefixtures("setup")
class TestE2E:
    @allure.title('D&R sitesinde kullanıcı girişi yapılarak sepete ürün ekleme işlemi test edilecektir.')
    def test_e2e(self):
        login = Login(self.driver)
        login.hover_login_button()
        login.click_login_button()
        login.accept_cookies()
        login.enter_email("denemehesabi299@outlook.com")
        login.enter_password("denemeQA159753")
        login.click_captcha()
        login.click_login_form()
        login.verify_successful_login("Hesabım")
        
        homepage = HomePage(self.driver)
        homepage.verify_homepage_opened("https://www.dr.com.tr/")
        homepage.hover_electronic_catalog()
        homepage.click_sub_categories()
        homepage.verify_sub_categories_opened("Cep Telefonları")
        homepage.click_first_product()
        homepage.verify_first_product_page_opened("Öne Çıkan Bilgiler")
        homepage.add_product_to_cart_button()
        homepage.verify_add_product_to_cart_item_control("Ürün alışveriş sepetinize eklendi")
        homepage.click_on_the_go_to_cart_button()

        basket = Basket(self.driver)
        basket.verify_basket_page_opened("Sepetim")
        