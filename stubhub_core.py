import sys
import datetime
import time
import requests
import importlib
from google.cloud import datastore
creds = importlib.import_module('creds')

PROJECT_ID = 'kochman-net-website'

def get_listings(event_id, qty_str, start_row, num_rows):
	event_id_str = str(event_id)
	start_row_str = str(start_row)
	num_rows_str = str(num_rows)
	URL='https://api.stubhub.com/search/inventory/v2?eventid=' + event_id_str + '&quantity=' + qty_str + '&start=' + start_row_str + '&rows=' + num_rows_str
	HEADERS = {'Authorization': creds.get_stubhub_key(PROJECT_ID)}	
	result = requests.get(URL, headers=HEADERS).json() # throws exception if no JSON returned
	return result