from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .browser import get_browser_session
import time

class LinkedInBot:
    def __init__(self):
        self.driver = get_browser_session().get_driver()

    def login(self, username, password):
        self.driver.get("https://www.linkedin.com/login")
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        WebDriverWait(self.driver, 10).until(EC.url_contains("/feed"))

    def connect(self, profile_url):
        self.driver.get(profile_url)
        time.sleep(2)
        try:
            connect_btn = self.driver.find_element(By.XPATH, "//button[contains(., 'Connect')]")
        except:
            dropdown = self.driver.find_element(By.XPATH, "//button[contains(@aria-label, 'More actions')]")
            dropdown.click()
            connect_btn = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//span[text()='Connect']/.."))
            )
        connect_btn.click()
        send_btn = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button/span[text()='Send']/.."))
        )
        send_btn.click()

    def check_connection_and_message(self, profile_url, message):
        self.driver.get(profile_url)
        time.sleep(2)
        try:
            msg_button = self.driver.find_element(By.XPATH, "//button[contains(., 'Message')]")
            msg_button.click()
            textarea = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@role,'textbox')]"))
            )
            textarea.send_keys(message)
            send_btn = self.driver.find_element(By.XPATH, "//button[@type='submit']")
            send_btn.click()
            return True
        except Exception:
            return False

    def close_session(self):
        get_browser_session().close()
