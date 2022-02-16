import asyncio
import json
#import json
from requests.auth import HTTPBasicAuth
#import requests
from time import sleep

import csv
import os
from difflib import SequenceMatcher

# Josephat Mwakyusa, February 15, 2022

# Addresses
DEST_BASE_URL = ''

# authentication
username = ''
password = ''

headers = {
'Content-type': 'application/json'
}


# import utilities
from utilities.get_server_access import get_user_name_and_password
from utilities.indicators import get_all_indicators_summary,get_indicator_details,get_expression_description


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

async def get_indicators_from_csv(file_path):
    users_data= []
    users_file = open(file_path)
    csv_arr_object = csv.reader(users_file)
    next(csv_arr_object)
    for user_data_row in csv_arr_object:
        users_data.append(user_data_row)
    return users_data

async def save_data_to_csv(rows, path):
    with open(path, 'w', encoding='UTF8') as file_to_write:
        writer = csv.writer(file_to_write)
        for row in rows:
            writer.writerow(row)

async def identify_duplicates(indicators):
    duplicates = []
    duplicates.append(["UID","Name","Duplicate UID","Duplicate Indicator Name"])
    path = os.getcwd()
    checked_indicators = {}
    path = path + '/metadata/duplicates.csv'
    for indicatorToCompare in indicators:
        numeEx = indicatorToCompare[2]
        denoEx = indicatorToCompare[4]
        checked_indicators[indicatorToCompare[0]] = indicatorToCompare[0]
        # print(checked_indicators)
        for indicator in indicators:
            if indicator[0] in checked_indicators:
                checked_indicators =  checked_indicators
            elif indicator[0] != indicatorToCompare[0]:
                duplicate = []
                numePMatch = similar(numeEx,indicator[2])
                denoPMatch = similar(denoEx,indicator[4])
                # print(numePMatch)
                # print(denoPMatch)
                if numePMatch == 1.0 and denoPMatch == 1.0 and indicator[0] not in checked_indicators:
                    checked_indicators[indicator[0]] = indicator[0]
                    duplicate.append(indicatorToCompare[0])
                    duplicate.append(indicatorToCompare[1])
                    duplicate.append(indicator[0])
                    duplicate.append(indicator[1])
                    # numeDescription = await get_expression_description(indicatorToCompare[1], DEST_BASE_URL)
                    print("MATCHED")
                    duplicates.append(duplicate)
                    response = await save_data_to_csv(duplicates, path)
    
async def main():
    shouldDownloadFirst =  input("Already downloaded indicators? (Yes/No): ")
    indicators = []
    if shouldDownloadFirst == 'No' or shouldDownloadFirst == '':
        server_access = await get_user_name_and_password()
        DEST_BASE_URL = server_access['url']
        username = server_access['username']
        password = server_access['password']
        indicators.append(["ID","Name","Numerator","Numerator Expression","Denominator","Denominator Expression","Indicator Type"])
        indicators_summary = await get_all_indicators_summary(DEST_BASE_URL,username,password)
        for indicator in indicators_summary['indicators']:
            indicator_details = await get_indicator_details(indicator['id'],DEST_BASE_URL,username,password)
            data = []
            data.append(indicator_details['id'])
            data.append(indicator_details['name'])
            data.append(indicator_details['numerator'])
            if 'numeratorDescription' in indicator_details:
                data.append(indicator_details['numeratorDescription'])
            data.append(indicator_details['denominator'])
            if 'denominatorDescription' in indicator_details:
                data.append(indicator_details['denominatorDescription'])
            data.append(indicator_details['indicatorType']['name'])
            indicators.append(data)
            path = os.getcwd()
            path = path + '/metadata/indicators.csv'
            response = await save_data_to_csv(indicators,path)
    else:
        path = os.getcwd()
        path = path + '/metadata/indicators.csv'
        indicators = await get_indicators_from_csv(path)

    # Identify duplicates 
    response = await identify_duplicates(indicators)


asyncio.run(main())
