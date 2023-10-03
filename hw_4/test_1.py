import time
import yaml
from testpage import OperationsHelper
import logging

with open('config.yaml') as f:
    # читаем документ YAML
    data = yaml.safe_load(f)

def test_1(get_browser):
    logging.info("Negative login test Starting")
    testpage = OperationsHelper(get_browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401", "Negative login test FAILED"

def test_2(get_browser):
    logging.info("Positive login test Starting")
    testpage = OperationsHelper(get_browser)
    testpage.go_to_site()
    testpage.enter_login(data["login"])
    testpage.enter_pass(data["pwd"])
    testpage.click_login_button()
    assert testpage.login_success() == f"Hello, {data['login']}", "Positive login test FAILED"

def test_3(get_browser):
    logging.info("Add post test Starting")
    testpage = OperationsHelper(get_browser)
    # testpage.go_to_site()
    # testpage.enter_login(data["login"])
    # testpage.enter_pass(data["pwd"])
    # testpage.click_login_button()
    time.sleep(data["sleep_time"])
    testpage.click_add_post_button()
    testpage.add_title("Title of new post")
    testpage.add_description("Description of new post")
    testpage.add_content("Content about new post")
    testpage.click_save_button()
    time.sleep(data["sleep_time"])
    testpage.find_new_post_title()
    assert testpage.find_new_post_title() == "Title of new post", "Add post test FAILED"


def test_4(get_browser):
    logging.info("Contact us Test Starting")
    testpage = OperationsHelper(get_browser)
    # testpage.go_to_site()
    # testpage.enter_login(data["login"])
    # testpage.enter_pass(data["pwd"])
    # testpage.click_login_button()
    # time.sleep(data["sleep_time"])
    testpage.click_contact_button()
    testpage.add_name(data["name"])
    testpage.add_email(data["email"])
    testpage.add_contact_content("Some information for site owners.")
    testpage.click_contact()
    time.sleep(data["sleep_time"])
    assert testpage.get_alert_message() == "Form successfully submitted", "Contact us Test FAILED!"

