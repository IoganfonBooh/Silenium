import requests
import json

baseURL = "https://petstore.swagger.io/v2"

status ='available'

# res = requests.get( f"{baseURL}/pet/findByStatus?status={status}", headers = {'accept': 'application/json'})
# print(res.text)
# print(res.status_code)
# print(res.json())
# print(type(res.json()))

# Post Create User

# headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
# data = {"id": 0,"username": "Joe","firstName": "string", "lastName": "string", "email": "string", "password":
#     "string", "phone": "string", "userStatus": 0}
#
# res = requests.post(f'{baseURL}/user', headers = headers, json=data)
#
# print(res.status_code)
# print(res.json())

# # GET- User by username


# res = requests.get(f"{baseURL}/user/Joe", headers = {'accept': 'application/json'})
#
#
# print(res.status_code)
# print(res.text)
#
# print(type(res.json()))

# Put- Updated User

# headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
# data = {"id": 0,"username": "Joe","firstName": "string", "lastName": "string", "email": "string",
#         "password":
#     "string", "phone": "string", "userStatus": 0}
#
# res = requests.put(f'{baseURL}/user/Tommy', json=data)
# print(res.status_code)
# print(res.json())


# DELETE user
headers = {'accept': 'application/json'}
res = requests.delete(f'{baseURL}/user/Tommy', headers = headers)
print(res.status_code)
print(res.text)