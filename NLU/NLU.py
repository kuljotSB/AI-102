#importing impportant libraries and utilities
import os
import requests
import json
from dotenv import load_dotenv

#loading the environment variables
load_dotenv()
prediction_url = os.getenv('PRED_URL')
lang_key = os.getenv('LANG_KEY')
request_id=os.getenv('REQUEST_ID')
api_key=os.getenv('API_KEY')
deployment=os.getenv('DEPLOYMENT')
project_name=os.getenv('PROJECT_NAME')

#defining the headers for our RESTful query
headers={
    'Ocp-Apim-Subscription-Key':lang_key,
    'Apim-Request-Id':request_id,
    'Content-Type':'application/json'
}

#taking input from the user
query=input('enter your query')
language=input('enter the language of your query')

#defining the body of our RESTful query
data = {
    "kind": "Conversation",
    "analysisInput": {
        "conversationItem": {
            "id": "1",
            "text": query,
            "modality": "text",
            "language": language,
            "participantId": "1"
        }
    },
    "parameters": {
        "projectName": project_name,
        "verbose": True,
        "deploymentName": deployment,
        "stringIndexType": "TextElement_V8"
    }
}

#making a call to our NLU model published with a prediction URL.
response = requests.post(prediction_url, headers=headers, data=json.dumps(data))

output=response.json()


top_intent =output['result']['prediction']['topIntent']

location=output['result']['prediction']['entities'][0]['text']

#making a call to the geocoding API to fetch the coordinates of a particular location
geocoding_url = 'http://api.openweathermap.org/geo/1.0/direct?q='+ str(location) +'&limit=5&appid=' +str(api_key)
geocoding_response=requests.get(geocoding_url).json()
latitude = geocoding_response[0]['lat']
longitude=geocoding_response[0]['lon']

#making a call to the weather API 
weather_url='https://api.openweathermap.org/data/2.5/weather?lat=' +str(latitude) +'&lon=' +str(longitude) +'&appid=' +str(api_key)
weather_response=requests.get(weather_url).json()
weather=weather_response['weather'][0]['description']
print('weather description of {} is {}'.format(location,weather))
