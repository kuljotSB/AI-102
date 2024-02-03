import os
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

load_dotenv()
endpoint = os.getenv("AZURE_LANG_ENDPOINT")
key=os.getenv("AZURE_LANG_KEY")

text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

documents = [
    """I had the best day of my life. I decided to go sky-diving and it made me appreciate my whole life so much more.
    I developed a deep-connection with my instructor as well, and I feel as if I've made a life-long friend in her."""
]



def analyze_sentiment():
    result = text_analytics_client.analyze_sentiment(documents, show_opinion_mining=True)
    print("let's analyze the sentiment of the document")
    docs = [doc for doc in result if not doc.is_error]
    for idx, doc in enumerate(docs):
       print(f"Overall sentiment: {doc.sentiment}")
       
       
def recognize_entity():
    result = text_analytics_client.recognize_entities(documents)
    print(result)
    
def extract_key_phrases():
    result = text_analytics_client.extract_key_phrases(documents)
    for idx, doc in enumerate(result):
    
        print("Key phrases in article #{}: {}".format(
            idx + 1,
            ", ".join(doc.key_phrases)
        ))
   
def detect_language():
    result = text_analytics_client.detect_language(documents)
    reviewed_docs = [doc for doc in result if not doc.is_error]
    
    print("Let's see what language each review is in!")

    for idx, doc in enumerate(reviewed_docs):
      print("document #{} is in '{}', which has ISO639-1 name '{}'\n".format(
        idx, doc.primary_language.name, doc.primary_language.iso6391_name
      ))
      


