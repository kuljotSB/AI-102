
prediction_url="YOUR_PREDICTION_URL"
key="YOUR_LANGUAGE_RESOURCE_KEY"

curl -X POST $prediction_url -H "Ocp-Apim-Subscription-Key: $key" -H "Content-Type: application/json" -d "{'question': 'what is microsoft QnA' }"
