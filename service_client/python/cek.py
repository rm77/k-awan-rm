import requests

ENDPOINT_URL='http://127.0.0.1:32000/notepads'

def get_all():
    uri = ENDPOINT_URL
    r = requests.get(uri)
    code = r.status_code
    if (code==200):
        result = r.json()
        return result
    else:
        return None


if __name__=='__main__':
    data = get_all()['data']
    for d in data:
        r = d['data']
        print(d['id'], r['date'], r['content'])

