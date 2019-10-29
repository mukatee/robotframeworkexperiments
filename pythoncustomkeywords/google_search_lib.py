from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class google_search_lib(object):
    driver = None

    @classmethod
    def get_driver(cls, browser):
        if cls.driver is not None:
            return cls.driver
        if (browser.lower()) == "chrome":
            cls.driver = webdriver.Chrome("../chromedriver")
        return cls.driver

    def __init__(self, browser):
        print("creating..")
        driver = google_search_lib.get_driver(browser)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def search_for(self, term):
        print("open")
        self.driver.get("http://google.com/")
        search_box = self.driver.find_element_by_name("q")
        search_box.send_keys(term)
        search_box.send_keys(Keys.RETURN)

    def close(self):
        self.driver.quit()
