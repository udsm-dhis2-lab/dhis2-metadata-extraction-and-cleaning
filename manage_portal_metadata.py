import asyncio
import json
#import json
from requests.auth import HTTPBasicAuth
#import requests
from time import sleep

import csv
import os

# import utilities
from utilities.get_server_access import get_user_name_and_password
from utilities.portal_slider import get_portal_slider_references,get_portal_slider_configs
from utilities.favorites import get_favorite_details

# Josephat Mwakyusa, February 14, 2022

# Addresses
DEST_BASE_URL = ''

# authentication
username = ''
password = ''

headers = {
'Content-type': 'application/json'
}


async def save_favorite_details_to_csv(rows):
    path = os.getcwd()
    with open(path + '/metadata/slider_favorites.csv', 'w', encoding='UTF8') as file_to_write:
        writer = csv.writer(file_to_write)
        for row in rows:
            writer.writerow(row)

async def main():
    server_access = await get_user_name_and_password()
    DEST_BASE_URL = server_access['url']
    username = server_access['username']
    password = server_access['password']
    metadata_rows = []
    metadata_rows.append(['Favorite name','Favorite ID', 'Favorite Type', 'Indicator/Dataelement', 'ID', 'Type'])
    portal_slider_references = await get_portal_slider_references(DEST_BASE_URL,username,password)
    for slider_key in portal_slider_references:
        portal_slider_configs = await get_portal_slider_configs(slider_key,DEST_BASE_URL,username,password)
        # print(json.dumps(portal_slider_configs))
        if 'chart' in portal_slider_configs:
            path = DEST_BASE_URL+ '/api/charts/' + portal_slider_configs['chart']['id'] + '.json?fields=id,name,dataDimensionItems[indicator[id,name],dataElement[id,name],programIndicator[id,name]]'
            favorite_data = await get_favorite_details(path, username,password)
            # print(json.dumps(favorite_data))
            for dataDimensionItem in favorite_data['dataDimensionItems']:
                if 'indicator' in dataDimensionItem:
                    metadata = []
                    metadata.append(favorite_data['name'])
                    metadata.append(favorite_data['id'])
                    metadata.append('CHART')
                    metadata.append(dataDimensionItem['indicator']['name'])
                    metadata.append(dataDimensionItem['indicator']['id'])
                    metadata.append('INDICATOR')
                    metadata_rows.append(metadata)
                elif 'dataElement' in dataDimensionItem:
                    metadata = []
                    metadata.append(favorite_data['name'])
                    metadata.append(favorite_data['id'])
                    metadata.append('CHART')
                    metadata.append(dataDimensionItem['dataElement']['name'])
                    metadata.append(dataDimensionItem['dataElement']['id'])
                    metadata.append('DATAELEMENT')
                    metadata_rows.append(metadata)
                elif 'programIndicator' in dataDimensionItem:
                    metadata = []
                    metadata.append(favorite_data['name'])
                    metadata.append(favorite_data['id'])
                    metadata.append('CHART')
                    metadata.append(dataDimensionItem['programIndicator']['name'])
                    metadata.append(dataDimensionItem['programIndicator']['id'])
                    metadata.append('PROGRAMINDICATOR')
                    metadata_rows.append(metadata)
        elif 'reportTable' in portal_slider_configs:
            path = DEST_BASE_URL+ '/api/reportTables/' + portal_slider_configs['reportTable']['id'] + '.json?fields=id,name,dataDimensionItems[indicator[id,name],dataElement[id,name],programIndicator[id,name]]'
            favorite_data = await get_favorite_details(path, username,password)
            for dataDimensionItem in favorite_data['dataDimensionItems']:
                if 'indicator' in dataDimensionItem:
                    metadata = []
                    metadata.append(favorite_data['name'])
                    metadata.append(favorite_data['id'])
                    metadata.append('CHART')
                    metadata.append(dataDimensionItem['indicator']['name'])
                    metadata.append(dataDimensionItem['indicator']['id'])
                    metadata.append('INDICATOR')
                    metadata_rows.append(metadata)
                elif 'dataElement' in dataDimensionItem:
                    metadata = []
                    metadata.append(favorite_data['name'])
                    metadata.append(favorite_data['id'])
                    metadata.append('CHART')
                    metadata.append(dataDimensionItem['dataElement']['name'])
                    metadata.append(dataDimensionItem['dataElement']['id'])
                    metadata.append('DATAELEMENT')
                    metadata_rows.append(metadata)
                elif 'programIndicator' in dataDimensionItem:
                    metadata = []
                    metadata.append(favorite_data['name'])
                    metadata.append(favorite_data['id'])
                    metadata.append('CHART')
                    metadata.append(dataDimensionItem['programIndicator']['name'])
                    metadata.append(dataDimensionItem['programIndicator']['id'])
                    metadata.append('PROGRAMINDICATOR')
                    metadata_rows.append(metadata)
        elif 'map' in portal_slider_configs:
            path = DEST_BASE_URL+ '/api/maps/' + portal_slider_configs['map']['id'] + '.json?fields=id,name,dataDimensionItems[indicator[id,name],dataElement[id,name],programIndicator[id,name]]'
            favorite_data = await get_favorite_details(path, username,password)
            for dataDimensionItem in favorite_data['dataDimensionItems']:
                if 'indicator' in dataDimensionItem:
                    metadata = []
                    metadata.append(favorite_data['name'])
                    metadata.append(favorite_data['id'])
                    metadata.append('CHART')
                    metadata.append(dataDimensionItem['indicator']['name'])
                    metadata.append(dataDimensionItem['indicator']['id'])
                    metadata.append('INDICATOR')
                    metadata_rows.append(metadata)
                elif 'dataElement' in dataDimensionItem:
                    metadata = []
                    metadata.append(favorite_data['name'])
                    metadata.append(favorite_data['id'])
                    metadata.append('CHART')
                    metadata.append(dataDimensionItem['dataElement']['name'])
                    metadata.append(dataDimensionItem['dataElement']['id'])
                    metadata.append('DATAELEMENT')
                    metadata_rows.append(metadata)
                elif 'programIndicator' in dataDimensionItem:
                    metadata = []
                    metadata.append(favorite_data['name'])
                    metadata.append(favorite_data['id'])
                    metadata.append('CHART')
                    metadata.append(dataDimensionItem['programIndicator']['name'])
                    metadata.append(dataDimensionItem['programIndicator']['id'])
                    metadata.append('PROGRAMINDICATOR')
                    metadata_rows.append(metadata)
        else :
            print("NOTHING")
    response = await save_favorite_details_to_csv(metadata_rows)

asyncio.run(main())
