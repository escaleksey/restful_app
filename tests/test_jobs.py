import requests
from pprint import pprint
from datetime import datetime

data = requests.get("http://127.0.0.1:5000/api/v2/job").json()
pprint(data)  # success

data = requests.get("http://127.0.0.1:5000/api/v2/job/6").json()
pprint(data)  # success

data = requests.get("http://127.0.0.1:5000/api/v2/job/2").json()
pprint(data)  # {'message': 'job 2 not found'}

json_data = {
    'team_leader': 2,
    'job': 'Student',
    'work_size': 4,
    'collaborators': '5, 2',
    'is_finished': True,
}

data = requests.post("http://127.0.0.1:5000/api/v2/job", json_data).json()
pprint(data)  # {'success': 'OK'}

json_data = {
    'team_leader': 2,
    'job': 'Student1',
    'work_size': 4,
}

data = requests.post("http://127.0.0.1:5000/api/v2/job", json_data).json()
pprint(data)
# {'message': {'collaborators': 'Missing required parameter in the JSON body or the post body or the query string'}}

