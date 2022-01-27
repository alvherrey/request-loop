import requests

def request(i):

    url = "http://192.168.9.11:9108/docreader/multipart"

    payload={}
    files=[
    ('front',('{}-f.jpeg'.format(i),open('{}-f.jpeg'.format(i),'rb'),'image/jpeg')),
    ('back',('{}-b.jpeg'.format(i),open('{}-b.jpeg'.format(i),'rb'),'image/jpeg'))
    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    return response.text