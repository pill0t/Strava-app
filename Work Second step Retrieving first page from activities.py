import pandas as pd
import requests
from pandas import json_normalize
import json
import csv  # Get the tokens from file to connect to Strava

with open('strava_tokens.json') as json_file:
    strava_tokens = json.load(json_file)  # Loop through all activities
url = "https://www.strava.com/api/v3/activities"
access_token = strava_tokens['access_token']  # Get first page of activities from Strava with all fields
r = requests.get(url + '?access_token=' + access_token)
r = r.json()

df = json_normalize(r)
df.to_csv('no_jest_wysoko.csv')

#----------------------------------------------------------------------------------------------------------------------
# The json file is in this app folder and should be updated. We can use it one time, and after that you should once
# again prepare it manually. Like on this website. First of all - "First step.py"
# https://medium.com/swlh/using-python-to-connect-to-stravas-api-and-analyse-your-activities-dummies-guide-5f49727aac86