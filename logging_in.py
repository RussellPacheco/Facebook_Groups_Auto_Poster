from selenium import webdriver
from .window import LoginFrame
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Log_in():
    def __init__(self, *args):
        self.fblogin_url = "https://www.facebook.com/"
        self.group_page_list = {"group_page_1": "", "group_page_2": "", "group_page_3": "" }
        self.driver = webdriver.Chrome("/drivers/chromedriver.exe")

    def log_in(self, *args):
        self.driver.get(self.fblogin_url)
        email_entry_field = self.driver.find_element_by_id("email").send_keys(email)
        password_entry_field = self.driver.find_element_by_id("pass").send_keys(password)
        confirm_button = self.driver.find_element_by_id("u_0_b").send_keys(Keys.ENTER)

    def access_group(self, *args):
        for i in len(group_urls):
            self.driver.get(group_urls[i])
            self.driver.find_element_by_class_name("n00je7tq arfg74bv qs9ysxi8 k77z8yql i09qtzwb n7fi1qx3 b5wmifdl hzruof5a pmk7jnqg j9ispegn kr520xx4 c5ndavph art1omkt ot9fgl3s rnr61an3").send_keys(Keys.ENTER)
            self.driver.find_element_by_class_name("_1mf _1mj").send_keys(post_text)
