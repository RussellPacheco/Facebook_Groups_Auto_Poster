from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


class Log_in():
    def __init__(self, email, password, url, post_text, image):
        self.email = email
        self.password = password
        self.url = url
        self.post_text = post_text
        self.image = image
        options = Options()
        options.headless = True

        self.driver = WebDriver(executable_path='driver/chromedriver.exe', port=0, options=options, service_args=None,
                                desired_capabilities=None, service_log_path=None, chrome_options=None,
                                keep_alive=True)
        # driver = webdriver.Chrome("drivers/chromedriver.exe", chrome_options=options)

        self.driver.get("https://www.facebook.com")
        email_entry_field = self.driver.find_element_by_id("email")
        email_entry_field.send_keys(self.email)
        password_entry_field = self.driver.find_element_by_id("pass")
        password_entry_field.send_keys(self.password)
        confirm_button = self.driver.find_element_by_id("u_0_b")
        confirm_button.send_keys(Keys.ENTER)
        self.access_group()
        time.sleep(3)

    def access_group(self):
        self.driver.get(self.url)
        self.driver.get(self.url)
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@class="mkhogb32"]').send_keys(self.image)
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@class="bi6gxh9e"]').send_keys(self.post_text)
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@aria-label="Post"]').send_keys(Keys.ENTER)
