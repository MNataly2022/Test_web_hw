"""
Задание
Условие: Добавить в проект тест по проверке механики работы формы Contact Us на главной странице личного кабинета. 
Должно проверятся открытие формы, ввод данных в поля, клик по кнопке и появление всплывающего alert.
Совет: переключиться на alert можно командой alert = self.driver.switch_to.alert
Вывести текст alert.text 
"""
import logging

import time
import yaml

from testpage import OperationsHelper

with open('config.yaml') as f:
    # читаем документ YAML
    data = yaml.safe_load(f)


def test_login(get_browser):
    logging.info("Login Test Starting")
    testpage = OperationsHelper(get_browser)
    testpage.go_to_site()
    testpage.enter_login(data["login"])
    testpage.enter_pass(data["pwd"])
    testpage.click_login_button()
    assert testpage.login_success() == f"Hello, {data['login']}", "Login Test FAILED"


def test_4(get_browser):
    logging.info("Contact us Test Starting")
    testpage = OperationsHelper(get_browser)
    # testpage.go_to_site()
    # testpage.enter_login(data["login"])
    # testpage.enter_pass(data["pwd"])
    # testpage.click_login_button()
    # time.sleep(data["sleep_time"])
    testpage.click_contact_button()
    testpage.add_name("Nataly")
    testpage.add_email("nmalova@mail.ru")
    testpage.add_contact_content("Some information for site owners.")
    testpage.click_contact_us_button()
    time.sleep(data["sleep_time"])
    assert testpage.get_alert_message() == "Form successfully submitted", "Contact us Test FAILED!"
