import httpx
from tools.fakes import get_randome_email

payload = {
    "email":get_randome_email(),
    "password":"string",
    "lastName":"string",
    "firstName":"string",
    "middleName":"string",
}

response = httpx.post("http://localhost:8000/api/v1/users", json=payload)

print(response.status_code)
print(response.json())

