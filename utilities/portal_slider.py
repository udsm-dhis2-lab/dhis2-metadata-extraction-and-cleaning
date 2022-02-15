
# Josephat Mwakyusa, February 14, 2022

import json
from requests.auth import HTTPBasicAuth
import requests

async def get_portal_slider_references(DEST_BASE_URL,username,password):
    response = requests.get(DEST_BASE_URL + '/api/dataStore/home-sliders', auth=(username,password), verify=False)
    if response.status_code != 200 and response.status_code != 201:
        print(response.status_code)
        return None
    else:
        return json.loads(response.content.decode('utf-8'))

async def get_portal_slider_configs(key,DEST_BASE_URL,username,password):
    response = requests.get(DEST_BASE_URL + '/api/dataStore/home-sliders/' + key, auth=(username,password), verify=False)
    if response.status_code != 200 and response.status_code != 201:
        print(response.status_code)
        return None
    else:
        return json.loads(response.content.decode('utf-8'))