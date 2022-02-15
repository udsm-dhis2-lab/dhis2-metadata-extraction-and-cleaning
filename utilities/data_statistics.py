# Josephat Mwakyusa, February 15, 2022

import json
from requests.auth import HTTPBasicAuth
import requests

async def get_portal_dashboards(DEST_BASE_URL,username,password):
    response = requests.get(DEST_BASE_URL + '/api/dataStore/dashboards', auth=(username,password), verify=False)
    if response.status_code != 200 and response.status_code != 201:
        print(response.status_code)
        return None
    else:
        return json.loads(response.content.decode('utf-8'))

async def get_portal_dashboards_details(key,DEST_BASE_URL,username,password):
    response = requests.get(DEST_BASE_URL + '/api/dataStore/dashboards/' + key, auth=(username,password), verify=False)
    if response.status_code != 200 and response.status_code != 201:
        print(response.status_code)
        return None
    else:
        return json.loads(response.content.decode('utf-8'))
