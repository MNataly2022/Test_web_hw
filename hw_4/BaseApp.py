import logging
import yaml
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

with open('config.yaml') as f:
    # читаем документ YAML
    data = yaml.safe_load(f)


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = data["address"]

    def find_element(self, locator, time=10):
        try:
            element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                             message=f"Can't find element by locator {locator}")
        except:
            logging.exception("Find element exception")
            element = None
        return element

    def get_element_property(self, locator, property):
        element = self.find_element(locator)
        if element:
            return element.value_of_css_property(property)
        else:
            logging.error(f"Property {property} not found in element with locator {locator}")
        return None

    def go_to_site(self):
        try:
            start_page = self.driver.get(self.base_url)
        except:
            logging.exception("Exception while open site")
            start_page = None
        return start_page

    def get_alert_text(self):
        try:
            alert = self.driver.switch_to.alert
            msg = alert.text
            alert.accept()
            return msg
        except:
            logging.exception("Exception with alert")
        return None
