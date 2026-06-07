from http import HTTPStatus
import json
from api.auth_api import registration_user, not_valid_registration, login_user, get_secure_page, get_catalog
import pytest

def test_registration(client):

    with open("test_data/auth_payload.json") as file:
        data= json.load(file)

    pld = data["registration_pld"]
    resp = registration_user(client, pld)

    assert resp.status_code == HTTPStatus.OK
    assert resp.url.path == "/user/registration/"
   
    assert "Пользователь с таким именем уже существует" in resp.text

def test_not_valid_registration(client):

    with open("test_data/auth_payload.json") as file:
        data = json.load(file)
    pld = data["not_valid_registration_pld"]
    resp = not_valid_registration(client, pld)

    assert resp.status_code == HTTPStatus.OK
    assert resp.url.path == "/user/registration/"
    
    email_errors = [
    "Введите корректный адрес электронной почты",
    "электронной почты",
    "Обязательное поле",
    "Enter a valid email address",
    "This field is required"
]

    assert any(error in resp.text for error in email_errors), f"Ни одна из ошибок email не найдена в ответе. Ответ бэка: {resp.text}"
    pass_errors = [
        "Введённый пароль слишком короткий",
        "Введённый пароль слишком широко распространён",
        "Введённый пароль состоит только из цифр"
    ]

    assert any(error in resp.text for error in pass_errors), f"Ни одна из ошибок пароля не найдена в ответе. Ответ бэка: {resp.text}"
    

def test_login(client):

    with open("test_data/auth_payload.json") as file:
        data= json.load(file)

    pld = data["login_pld"]
    resp = login_user(client, pld)

    assert resp.status_code == HTTPStatus.FOUND  
    
    
    assert resp.headers.get("Location") == "/"
    
    assert "sessionid" in client.cookies


def test_catalog(client):

    resp = get_catalog(client)

    assert resp.status_code == HTTPStatus.MOVED_PERMANENTLY

@pytest.fixture
def auth_client(client):
    with open("test_data/auth_payload.json") as file:
        data = json.load(file)
    pld = data["login_pld"]

    resp = login_user(client, pld)
    
        
    return client 

def test_profile(auth_client):

    resp = auth_client.get("/user/profile/") 
    
    assert resp.status_code == HTTPStatus.OK
    
    assert "Профиль" in resp.text

  