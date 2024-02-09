#type in "pip install azure-ai-formrecognizer" in your integrated terminal in VSCode to install the Azure Doc Client library for python
#importing important libraries and utilities
import os
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
from openai import AzureOpenAI
from dotenv import load_dotenv

#importing the environment variables
load_dotenv()
form_endpoint=os.getenv('FormEndpoint')
form_key=os.getenv('FormKey')

#defining the document contained in the url
document_url="https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/sample-invoice.pdf"

#creating a document analysis client
document_analysis_client=DocumentAnalysisClient(endpoint=form_endpoint, credential=AzureKeyCredential(form_key))
poller = document_analysis_client.begin_analyze_document_from_url("prebuilt-invoice", document_url)
invoices=poller.result()

#extracting the fields from the document
for idx,invoice in enumerate(invoices.documents):
    vendor_name=invoice.fields.get("VendorName")
    vendor_name_value=vendor_name.value
    
    vendor_address = invoice.fields.get("VendorAddress")
    vendor_address_value=vendor_address.value
    
    invoice_date=invoice.fields.get("InvoiceDate")
    invoice_date_value = invoice_date.value
    
    subtotal=invoice.fields.get("SubTotal")
    subtotal_value=subtotal.value
    
#printing the extracted fields
print('vendor_name:',vendor_name_value) 
print('vendor_address:',vendor_address_value)
print('invoice_date:',invoice_date_value)
print('subtotal:',subtotal_value)
