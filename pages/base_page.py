from selenium.webdriver.support import expected_conditions 
from selenium.webdriver.support.wait import WebDriverWait
from constants.home_page_locator import *
from selenium.webdriver.common.action_chains import ActionChains
import os
import allure
import time

class PageBase:
    def __init__(self, driver):
        self.driver = driver
    
    #Verilen locator görünür olmasını bekler.   
    def wait_element_visibility(self, locator):
        return WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(locator))
    
    #Verilen locator için tıklama işlemini gerçekleştirir.    
    def click_element(self,locator):
        self.wait_element_visibility(locator).click()
    
    #Verilen locator için yazı girme işlemini gerçekleştirir.
    def send_keys_element(self,locator,text):
        self.wait_element_visibility(locator).send_keys(text)
      
    def hover_over_element(self, locator):
        item = self.wait_element_visibility(locator)
        action = ActionChains(self.driver)
        action.move_to_element(item).perform()
    
    def send_keys_input(self,locator,text):
        self.wait_element_visibility(locator).send_keys(text)
    
    def find_element(self,locator):
        return self.driver.find_element(*locator)
    
    #Verilen liste locator'ı sayfa içinde bulma işlemini gerçekleştirir. 
    def find_elements(self,locator):
        return self.driver.find_elements(*locator)
    
    #Çerezleri kabul etmek için kullanılır.
    def accept_cookies(self):
        time.sleep(0.8)
        self.click_element(COOKIES)
    
    #Sayfayı aşağıya doğru kaydırmak için kullanılır.
    def scroll_down(self, pixels):
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")
        
    # Verilen sayfa numarasına geçmek için kullanılır.    
    def switch_to_window(self,page):
        self.driver.switch_to.window(self.driver.window_handles[page])
    
    #Ekran görüntüsü almak için kullanılır.    
    def take_screenshot(self, screenshotName):
        time.sleep(0.8)
        file_path = os.path.join("screenshot", screenshotName)
        self.driver.save_screenshot(file_path)
        with open(file_path, 'rb') as f:
            allure.attach(f.read(), name=screenshotName, attachment_type=allure.attachment_type.PNG)
            
    