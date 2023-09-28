"""
Задание 1.
Добавить в тестовый проект шаг добавления
поста после входа. Должна выполняться
проверка на наличие названия поста на странице
сразу после его создания.
💡 Совет:
Не забудьте добавить небольшие ожидания
перед и после нажатия кнопки создания поста.
"""

import time
import yaml

with open('config.yaml') as f:
    # читаем документ YAML
    data = yaml.safe_load(f)
    browser = data["browser"]


def test_1(site, x_selector1, x_selector2, x_selector4, btn_selector, add_post_selector, add_title, add_description,
           add_content, save_post, check_title):
    input1 = site.find_element("xpath", x_selector1)
    input1.clear()
    input1.send_keys(data["login"])
    input2 = site.find_element("xpath", x_selector2)
    input2.clear()
    input2.send_keys(data["pwd"])
    btn = site.find_element("css", btn_selector)
    btn.click()

    time.sleep(data["sleep_time"])

    btn = site.find_element("xpath", add_post_selector)
    btn.click()

    input3 = site.find_element("xpath", add_title)
    input3.clear()
    input3.send_keys("Title of new post")
    input4 = site.find_element("xpath", add_description)
    input4.clear()
    input4.send_keys("Description of new post")
    input5 = site.find_element("xpath", add_content)
    input5.clear()
    input5.send_keys("Content about new post")
    btn = site.find_element("xpath", save_post)
    btn.click()

    time.sleep(data["sleep_time"])

    code_label = site.find_element("xpath", check_title).text
    assert code_label == "Title of new post", "test 'add post' Failed"
