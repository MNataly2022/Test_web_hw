import yaml
from selenium.webdriver.support import expected_conditions as exp_cond
from selenium.webdriver.support.wait import WebDriverWait

with open('config.yaml') as f:
    # читаем документ YAML
    data = yaml.safe_load(f)


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = data["address"]

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(exp_cond.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def get_element_property(self, locator, property):
        element = self.find_element(locator)
        return element.value_of_css_property(property)

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def get_alert_txt(self):
        alert = self.driver.switch_to.alert
        msg = alert.text
        alert.accept()
        return msg
