import requests

base_url = 'http://localhost:8080/api/v3'

def get_api_data(endpoint):
    response = requests.get(f'{base_url}{endpoint}')
    return response