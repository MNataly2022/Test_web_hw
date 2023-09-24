"""
Написать тест с использованием pytest и requests, в котором:
Адрес сайта, имя пользователя и пароль хранятся в config.yaml
conftest.py содержит фикстуру авторизации по адресу https://test-stand.gb.ru/gateway/login с передачей параметров
“username" и "password" и возвращающей токен авторизации
Тест с использованием DDT проверяет наличие поста с определенным заголовком в списке постов другого пользователя,
для этого выполняется get запрос по адресу https://test-stand.gb.ru/api/posts c хедером, содержащим токен авторизации
в параметре "X-Auth-Token". Для отображения постов другого пользователя передается "owner": "notMe".
"""

import requests
import yaml

with open('config.yaml') as f:
    # читаем документ YAML
    data = yaml.safe_load(f)


def login():
    response = requests.post(data["url_login"],
                             data={'username': data["login"], 'password': data["password"]})
    if response.status_code == 200:
        return response.json()["token"]


def get(token):
    resource = requests.get(data["url_posts"],
                            headers={"X-Auth-Token": token},
                            params={"owner": "notMe"})
    return resource.json()


def post(token):
    resource = requests.post(data["url_posts"],
                             headers={"X-Auth-Token": token},
                             data={'username': data["login"], 'password': data["password"],
                                   'title': 'New Post Title', 'description': 'New Post Description',
                                   'content':'Story about some news.'})
    return resource.json()


if __name__ == '__main__':
    print(get(login))
