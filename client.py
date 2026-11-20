import requests

Url ="http://localhost:8000"
user_credentials = {"username": "atria2", "password": "123456789" , "role": "staff"}
response = requests.post(url=Url+"/register", json=user_credentials)
print(response.status_code)
print(response.json())

response = requests.post(url=Url+"/login", json=user_credentials)
response_json = response.json()
access_token = response_json.get("access_token")
refresh_token = response_json.get("refresh_token")

header ={"token":access_token}
response = requests.get(url=Url+"/packages", headers=header)
print(response.json())

header ={"token":access_token}
response = requests.get(url=Url+"/packages/2", headers=header)
print(response.json())

header ={"token":access_token}
update ={"status": "delivered"}
response = requests.patch(url=Url+"/packages/2", headers=header, json=update)
print(response.json())

header ={}