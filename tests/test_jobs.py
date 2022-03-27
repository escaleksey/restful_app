import requests
from pprint import pprint
from datetime import datetime
'''data = requests.get("http://127.0.0.1:5000/api/jobs").json()
pprint(data)

data = requests.get("http://127.0.0.1:5000/api/jobs/1").json()
pprint(data)

data = requests.get("http://127.0.0.1:5000/api/jobs/asdasd").json()
pprint(data)

print(str(datetime.now()))
json_data = {
        'id': 6,
        'team_leader': 1,
        'job': 'New Super Job',
        'work_size': 2,
        'collaborators': '3, 2',
        'end_date': '',
        'start_date': '',
        'is_finished': True
}

response = requests.post("http://127.0.0.1:5000/api/jobs", json=json_data)
pprint(response.json())

json_data = {
        'id': 6,
        'team_leader': 1,
        'job': 'New Super Job',
        'work_size': 2,
        'collaborators': '3, 2',
        'end_date': '',
        'start_date': '',
        'is_finished': True
}

response = requests.post("http://127.0.0.1:5000/api/jobs", json=json_data)
pprint(response.json())
json_data = {
        'id': 6,
        'job': 'New Super Job',
        'work_size': 2,
        'collaborators': '3, 2',
        'end_date': '',
        'start_date': '',
}

response = requests.post("http://127.0.0.1:5000/api/jobs", json=json_data)
pprint(response.json())
json_data = {
        'id': 6,
        'team_leader': 1,
        'job': 2,
        'work_size': 2,
        'collaborators': '3, 2',
        'end_date': '',
        'start_date': '',
        'is_finished': True
}

response = requests.post("http://127.0.0.1:5000/api/jobs", json=json_data)
pprint(response.json())'''
json_data = {
        'id': 6,
        'team_leader': 'Name',
        'job': 'New Super Job',
        'work_size': 2,
        'collaborators': '3, 2',
        'end_date': '',
        'start_date': '',
        'is_finished': True
}

response = requests.post("http://127.0.0.1:5000/api/jobs", json=json_data)
pprint(response.json()) # Создание работы для изменения
response = requests.put("http://127.0.0.1:5000/api/jobs/999", json=json_data)
pprint(response.json()) # {'error': 'Not found'}
json_data = {
        'team_leader': 'NewName',
        'job': 'Update New Super Job',
        'work_size': 3,
        'collaborators': '3, 2',
        'is_finished': True
}
missing_json_data = {
        'new_arg': '1'
}
empty_json_data = {}
response = requests.put("http://127.0.0.1:5000/api/jobs/6", json=json_data)
pprint(response.json())  # {'success': 'OK'}
response = requests.put("http://127.0.0.1:5000/api/jobs/6", json=empty_json_data)
pprint(response.json()) # {'error': 'Empty request'}
response = requests.put("http://127.0.0.1:5000/api/jobs/6", json=missing_json_data)
pprint(response.json()) # {'error': 'Bad request'}