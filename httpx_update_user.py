import httpx

from tools.fakers import get_random_email


create_user_data = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_data)
create_user_response_data = create_user_response.json()

login_data = {
    "email": create_user_data["email"],
    "password": create_user_data["password"]
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_data)
login_response_data = login_response.json()
login_access_token = login_response_data["token"]["accessToken"]

update_data = {
    "email": get_random_email(),
    "lastName": "Пушкин",
    "firstName": "Александр",
    "middleName": "Сергеевич"
}

headers = {"Authorization": f"Bearer {login_access_token}"}

update_response = httpx.patch(
    f"http://localhost:8000/api/v1/users/{create_user_response_data['user']['id']}",
    headers=headers, json=update_data
)
update_user_data = update_response.json()

print("New user data:", update_user_data)