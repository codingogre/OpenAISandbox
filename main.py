import os
import requests
import json
import openai

openai.api_key = os.getenv("AZURE_OPENAI_KEY")
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT") # your endpoint should look like the following https://YOUR_RESOURCE_NAME.openai.azure.com/
openai.api_type = 'azure'
openai.api_version = '2023-05-15' # this may change in the future

deployment_name = 'GPT-turbo' #This will correspond to the custom name you chose for your deployment when you deployed a model.

print('openai.api_key: ' + openai.api_key)
print('openai.api_base: ' + openai.api_base)

# Send a completion call to generate an answer
print('Sending a test query')
start_phrase = 'When was Elasticsearch created?'
response = openai.Completion.create(engine=deployment_name, prompt=start_phrase, max_tokens=100)
text = response['choices'][0]['text'].replace('\n', '').replace(' .', '.').strip()
print('Query: ', start_phrase)
print('Answer: ', response)