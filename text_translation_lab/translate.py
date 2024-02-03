#importing important utilities and libraries
import os
import requests
from dotenv import load_dotenv
import json

#loading important environment variables and configurations
load_dotenv()
key = os.getenv("TRANSLATOR_KEY")
endpoint = os.getenv("TRANSLATOR_ENDPOINT")
location = os.getenv("TRANSLATOR_LOCATION")

#constructing the URL for our RESTful query
path='translate'
constructed_url = endpoint + path

#taking input from the user
language=input("enter the target language")

#setting the parameters for our RESTful query
params={
    'api-version':'3.0',
    'from':'en',
    'to': [language]
}

#setting the headers for our RESTful query
headers = {
    'Ocp-Apim-Subscription-Key': key,
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
}

#setting the body of our RESTful query
body = [{
    'text': 'I would really like to drive your car around the block a few times!'
}]

#making a call to the translator API
request = requests.post(constructed_url, params=params, headers=headers, json=body)
response = request.json()
print(response[0]['translations'][0]['text'])
