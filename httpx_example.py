import httpx

#
# response = httpx.get('https://jsonplaceholder.typicode.com/todos/1')
#
# print(response.status_code)
# print(response.json())
#
# data = {
#     "title":"Новая задача",
#     "completed":False,
#     "userid": 1
# }
#
#
# response = httpx.post('https://jsonplaceholder.typicode.com/todos/', json=data)
# print(response.status_code)
# print(response.json())
#
#
# data = {
#     "usermane":"test_user",
#     "password":"12345"
# }
#
# response = httpx.post('https://httpbin.org/post',data=data)
# print(response.status_code)
# print(response.json())
#
#
# headers = {"Autorization":"Berarer my_secret_token"}
# response = httpx.get("https://httpbin.org/get",headers=headers)
# print(response.request.headers)
# print(response.json())
#
# params = {"userid":1}
# response =httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)
# print(response.url)
# print(response.json())
#
#
# files = {"file": ("user_service.proto", open("user_service.proto", "rb"))}
# response = httpx.post("https://httpbin.org/post", files=files)
#
# print(response.json())
#
#
# with httpx.Client() as client:
#     response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
#     response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")
#
#     print(response1.json())
#     print(response2.json())
#
#
# client = httpx.Client(headers={"Autorization":"Berarer my_secret_token"})
# response = client.get("https://httpbin.org/get")
#
# print(response.json())

try:
    response = httpx.get("https://jsonplaceholder.typicode.com/todos/invalid-url")
    response.raise_for_status()
except httpx.HTTPStatusError as e:
    print(f"Ошибка запроса: {e}")


try:
    response = httpx.get("https://httpbin.org/delay/5", timeout=2)
    response.raise_for_status()
except httpx.ReadTimeout as e:
    print(f"Запрос выполнялся больше установленного")