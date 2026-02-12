import httpx

login_user = {
  "email": "spiritqa@ya.com",
  "password": "1234567890"
}

with httpx.Client() as client:
    login_response = client.post("http://localhost:8000/api/v1/authentication/login",json=login_user)
    login_response_data = login_response.json()
    print(login_response.status_code)
    print(login_response_data)
    access_token = login_response_data["token"]["accessToken"]
    response = client.get("http://localhost:8000/api/v1/users/me",headers = {"Authorization": f"Bearer {access_token}"})
    print(response.status_code)
    print(response.json())
