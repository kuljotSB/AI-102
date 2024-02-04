#importing important libraries and utilities
import os
import requests
import json
from dotenv import load_dotenv

#loading important configurations and environment variables
load_dotenv()
endpoint = os.getenv('ENDPOINT')
key = os.getenv('KEY')

#defining the url for POST request
url = str(endpoint) + "computervision/imageanalysis:analyze"

#defining the headers for the POST request
headers = {
    "Ocp-Apim-Subscription-Key": key,
    "Content-Type": "application/json",
}

#defing the parameters for the POST request
params = {
    "features": "caption,read,tags,people",
    "model-version": "latest",
    "language": "en",
    "api-version": "2023-10-01"
   
}

#defining the data for the POST request
data = {
    "url": "https://learn.microsoft.com/azure/ai-services/computer-vision/media/quickstarts/presentation.png"
}

#storing the response from the POST request
response = requests.post(url, headers=headers, params=params, json=data).json()

#defining the function to caption the image
def caption_the_image():
    caption = response['captionResult']['text']
    print('the caption for the image is: {}'.format(caption))
  
#defining the function to generate tags and keywords for the image  
def list_out_all_the_tags():
    array = response['tagsResult']['values']
    length = len(array)
    i=0
    print('all the tags for the image are:')
    while i<length:
        print(response['tagsResult']['values'][i]['name'] + '\n')
        i=i+1
        

#defing the function to list out all the people in the image
def show_people():
    print(response['peopleResult']['values'])
    








