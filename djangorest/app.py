import requests
import json
data={'name':'Ashish',
'password':'123'}
json_data=json.dumps(data)
r=requests.get("http://127.0.0.1:8000/api/create/?username=Ashish&password=123")
r2=requests.get("http://127.0.0.1:8000/api/details/4/?username=Ashish&password=123")
print(r.json())
print(r.status_code)
print(r2.json())
r3=requests.get("http://127.0.0.1:8000/api/login/?username=Ashish&password=123")
print(r3.json())
print(r3.status_code)