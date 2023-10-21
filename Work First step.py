#                                                       111111111111111111

#First step. This code is to prepare file named strava_tokens.json. Which you will need in next step
#So this is NUMBER ONE
#-------------------------------------------------------------------------------------------------------
import requests
import json# Make Strava auth API call with your
import os
from dotenv import load_dotenv
# client_code, client_secret and code

load_dotenv()

response = requests.post(
                    url = 'https://www.strava.com/oauth/token',
                    data = {
                            'client_id': os.getenv("client_id"), #Insert here your Client ID from strava
                            'client_secret': os.getenv("client_secret"), #Here your client secret
                            'code': os.getenv("code"), #Here you should insert code from url - there is explanation https://medium.com/swlh/using-python-to-connect-to-stravas-api-and-analyse-your-activities-dummies-guide-5f49727aac86
                            'grant_type': 'authorization_code'
                            }
# In this case if you will have response in console like this "{'message': 'Bad Request'... - it means that you used this 'code' recently, and you need another one
                )#Save json response as a variable
strava_tokens = response.json()# Save tokens to file
with open('strava_tokens.json', 'w') as outfile:
    json.dump(strava_tokens, outfile)# Open JSON file and print the file contents
# to check it's worked properly
with open('strava_tokens.json') as check:
  data = json.load(check)
print(data)