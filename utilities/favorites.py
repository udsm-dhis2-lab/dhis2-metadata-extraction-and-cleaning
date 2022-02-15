
# Josephat Mwakyusa, February 15, 2022

import json
from requests.auth import HTTPBasicAuth
import requests

async def get_favorite_details(PATH,username,password):
    response = requests.get(PATH, auth=(username,password), verify=False)
    if response.status_code != 200 and response.status_code != 201:
        print(response.status_code)
        return None
    else:
        return json.loads(response.content.decode('utf-8'))
