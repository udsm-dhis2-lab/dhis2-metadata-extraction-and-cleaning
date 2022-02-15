import asyncio
import json
#import json
from requests.auth import HTTPBasicAuth
#import requests
from time import sleep

# import utilities
from utilities.get_server_access import get_user_name_and_password
from utilities.portal_slider import get_portal_slider_references,get_portal_slider_configs

# Josephat Mwakyusa, February 14, 2022

# Addresses
DEST_BASE_URL = ''

# authentication
username = ''
password = ''

headers = {
'Content-type': 'application/json'
}

async def main():
    server_access = await get_user_name_and_password()
    DEST_BASE_URL = server_access['url']
    username = server_access['username']
    password = server_access['password']
    portal_slider_references = await get_portal_slider_references(DEST_BASE_URL,username,password)
    for slider_key in portal_slider_references:
        portal_slider_configs = await get_portal_slider_configs(slider_key,DEST_BASE_URL,username,password)
        print(json.dumps(portal_slider_configs))


asyncio.run(main())
