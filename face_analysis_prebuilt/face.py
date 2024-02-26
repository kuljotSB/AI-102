#importing important libraries and utilities
import os
import json
import requests
import uuid
import dotenv
from dotenv import load_dotenv

#loading the environment variables
load_dotenv()
endpoint=os.getenv("ENDPOINT")
key=os.getenv("KEY")

url = str(endpoint)+"vision/v3.1/analyze"

headers={
    "Content-Type":"application/json",
    "Ocp-Apim-Subscription-Key":key
}

data_body={
    "url":"https://upload.wikimedia.org/wikipedia/en/b/be/Disloyal_man_with_his_girlfriend_looking_at_another_girl.jpg"
}

response = requests.post(url, headers=headers, json=data_body).json()

print(response)
