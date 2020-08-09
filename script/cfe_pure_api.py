import json
import requests


BASE_URL = "http://127.0.0.1:8000/"

ENDPOINT = "api/updates/"

def get_list():
    r = requests.get(BASE_URL + ENDPOINT)
    data = r.json()
    print(type(json.dumps(data)))
    for obj in data:
        # print(obj['id'])
        if(obj['id']==1):
            r = requests.get(BASE_URL + ENDPOINT + str(obj['id']) + '/')
            print(r.json())
    return data

def create_update():
    new_data = {
        'user': 1,
        'content':'cool update'
    }
    r = requests.post(BASE_URL + ENDPOINT, data=new_data)
    print(r.headers)
    if r.status_code  == requests.codes.ok:
        # print(r.json())
        return(r.json())
    return r.text



# print(get_list())

print(create_update())