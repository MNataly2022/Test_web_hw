"""
Добавить в задание с REST API еще один
тест, в котором создается новый пост,
а потом проверяется его наличие на сервере
по полю “описание”.
💡 Подсказка:
Создание поста выполняется запросом
к https://test-stand.gb.ru/api/posts с передачей
параметров title, description, content.
"""
from checkers import login, post


def test_1(login):
    res = post(login)
    lst_desc = res["description"]
    assert 'news' in lst_desc, "тест провален"


def test_2(login):
    res = post(login)
    lst_desc = res["description"]
    assert 'New' in lst_desc, "тест провален"
