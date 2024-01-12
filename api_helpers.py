import requests

base_url = 'http://localhost:8080/api/v3'

def get_api_data(endpoint, params = {}):
    response = requests.get(f'{base_url}{endpoint}', params=params)
    return response