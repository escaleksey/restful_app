import requests
from pprint import pprint
from datetime import datetime
from data.users import User


data = requests.get("http://127.0.0.1:5000/api/v2/user").json()
pprint(data) # success

data = requests.get("http://127.0.0.1:5000/api/v2/user/999").json()
pprint(data)  # not found

data = requests.get("http://127.0.0.1:5000/api/v2/user/2").json()
pprint(data) # success

json_data = {
    'name': 'New Name',
    'about': 'Info about me',
    'email': 'email@mail.com',
    'hashed_password': 'password',
    'created_date': datetime.now()
}
data = requests.post("http://127.0.0.1:5000/api/v2/user", json_data).json()
pprint(data) # {'success': 'OK'}

json_data = {
    'name': 'New Name',
    'about': 'Info about me',
    'email': 'email@mail.com',
    'hashed_password': 'password',
    'created_date': datetime.now()
}
data = requests.post("http://127.0.0.1:5000/api/v2/user", json_data).json()
pprint(data)  # {'error': 'this email is already in use'}

json_data = {
    'name': 'New Name',
    'about': 'Info about me',
    'hashed_password': 'password',
    'created_date': datetime.now()
}
data = requests.post("http://127.0.0.1:5000/api/v2/user", json_data).json()
pprint(data)
# {'message': {'email': 'Missing required parameter in the JSON body or the post body or the query string'}}

json_data = {
    'name': 'New Name',
    'about': 'Info about me',
    'email': 'email1@mail.com',
    'hashed_password': 'password',
    'created_date': datetime.now(),
    'test': 'test'
}
data = requests.post("http://127.0.0.1:5000/api/v2/user", json_data).json()
pprint(data)  # {'success': 'OK'} test был проигнорирован
