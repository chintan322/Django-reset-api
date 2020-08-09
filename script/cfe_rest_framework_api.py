import requests
import json

ENDPOINT = "http://127.0.0.1:8000/api/status/"

def do(method='get', data={}, is_json=True):
    headers = {}
    if is_json:
        headers['content-type'] = 'application/json'
        data = json.dumps(data)
    r = requests.request(method, ENDPOINT, data=data, headers=headers)
    print(r.text)
    print(r.status_code)
    return r

# do(data={'id':500})

# do(method='delete',data={'id':500})

# do(method='put',data={'id':7, "content":"Some new content","user":1})

do(method='put',data={"content":"Some new content","user":1})

#create
#retrieve / list
#update
#delete


# r = requests.request("get", "http://127.0.0.1:8000/api/status/?id=" + str(id), data={'id':6})