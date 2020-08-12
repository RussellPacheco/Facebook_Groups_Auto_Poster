from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Log_in(WebDriver):
        WebDriver.__init__((executable_path='chromedriver', port=0, options=None, service_args=None, desired_capabilities=None, service_log_path=None, chrome_options=None, keep_alive=True)
        driver = webdriver.Chrome("drivers/chromedriver.exe")

        driver.get("https://www.facebook.com")
        email_entry_field = driver.find_element_by_id("email")
        email_entry_field.send_keys(email)
        password_entry_field = driver.find_element_by_id("pass")
        password_entry_field.send_keys(password)
        confirm_button = driver.find_element_by_id("u_0_b")
        confirm_button.send_keys(Keys.ENTER)


    def access_group(self, url, post_text):
            driver.get(url)
            driver.find_element_by_class_name("n00je7tq arfg74bv qs9ysxi8 k77z8yql i09qtzwb n7fi1qx3 b5wmifdl hzruof5a pmk7jnqg j9ispegn kr520xx4 c5ndavph art1omkt ot9fgl3s rnr61an3").send_keys(Keys.ENTER)
            driver.find_element_by_class_name("_1mf _1mj").send_keys(post_text)
            driver.find_element_by_class_name("n00je7tq arfg74bv qs9ysxi8 k77z8yql i09qtzwb n7fi1qx3 b5wmifdl hzruof5a pmk7jnqg j9ispegn kr520xx4 c5ndavph art1omkt ot9fgl3s rnr61an3").send_keys(Keys.ENTER)
