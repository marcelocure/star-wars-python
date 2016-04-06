import requests
import json
import config

base_url = config.STAR_WARS_API_BASE_URL


def post(endpoint, payload):
    headers = {'content-type': 'application/json'}
    response = requests.post('{0}/{1}'.format(base_url, endpoint), data=json.dumps(payload), headers=headers)
    return json.loads(json.dumps(response.json()))


def get_all(endpoint):
    response = requests.get('{0}/{1}'.format(base_url, endpoint))
    return json.loads(json.dumps(response.json()))['results']


def get(endpoint, id):
    url = '{0}/{1}/{2}'.format(base_url, endpoint, id)
    response = requests.get(url)
    return json.loads(json.dumps(response.json()))


def delete(endpoint, id):
    response = requests.delete('{0}/{1}/{2}'.format(base_url, endpoint, id))
    return json.loads(json.dumps(response.json()))


def put(endpoint, payload, id):
    response = requests.put('{0}/{1}/{2}'.format(base_url, endpoint, id), payload)
    return json.loads(json.dumps(response.json()))
