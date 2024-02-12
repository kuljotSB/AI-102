#pip install azure-search-documents
#importing important utilities and libraries
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
import os
from dotenv import load_dotenv
import requests

#loading the environment variables
load_dotenv()
service_endpoint = os.getenv('AZURE_SEARCH_SERVICE_ENDPOINT')
index_name = os.getenv('AZURE_SEARCH_INDEX_NAME')
key = os.getenv('AZURE_SEARCH_API_KEY')

#creating an Azure Search client
search_client = SearchClient(service_endpoint, index_name, AzureKeyCredential(key))

#fetching the results
results = search_client.search(search_text="2023")

#printing the PII entities
print('the pii entities are:')
for result in results:
    for entities in result['pii_entities']:
        print('entity: {} of type {}'.format(entities['text'],entities['type']))
    

