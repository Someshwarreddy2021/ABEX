import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options

class BrowserSession:
    def __init__(self):
        options = uc.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-blink-features=AutomationControlled")
        self.driver = uc.Chrome(options=options)
        self.driver.implicitly_wait(10)

    def get_driver(self):
        return self.driver

    def close(self):
        self.driver.quit()


browser_session = None

def get_browser_session():
    global browser_session
    if browser_session is None:
        browser_session = BrowserSession()
    return browser_session
