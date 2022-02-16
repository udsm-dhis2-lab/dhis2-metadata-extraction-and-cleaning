
# Josephat Mwakyusa, February 14, 2022

import json
from requests.auth import HTTPBasicAuth
import requests

async def get_all_indicators_summary(DEST_BASE_URL,username,password):
    response = requests.get(DEST_BASE_URL + '/api/indicators.json?fields=id,name&paging=false', auth=(username,password), verify=False)
    if response.status_code != 200 and response.status_code != 201:
        print(response.status_code)
        return None
    else:
        return json.loads(response.content.decode('utf-8'))


async def get_indicator_details(id,DEST_BASE_URL,username,password):
    response = requests.get(DEST_BASE_URL + '/api/indicators/' + id + '.json?fields=id,name,description,numerator,numeratorDescription,denominator,denominatorDescription,indicatorType[id,name]', auth=(username,password), verify=False)
    if response.status_code != 200 and response.status_code != 201:
        print(response.status_code)
        return None
    else:
        return json.loads(response.content.decode('utf-8'))

async def get_expression_description(payload, URL,username,password,headers):
    response = requests.post(URL, auth = HTTPBasicAuth(username,password), headers=headers, data=payload)
    if response.status_code != 200 and response.status_code != 201:
        print(response.status_code)
        return None
    else:
        return json.loads(response.content.decode('utf-8'))
