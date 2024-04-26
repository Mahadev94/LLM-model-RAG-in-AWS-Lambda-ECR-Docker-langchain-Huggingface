import os
import json
import sys
import boto3
print('imported successfully..........')

promt='''
You are smart Assistant so please let me know machine learning is smartest way?
'''
bedrock=boto3.client(service_name='bedrock-runtime')
payload={

}
body=json.dumps(payload)
model_id="meta.llama2-70b-chat-v1"

response=bedrock.invoke_model(
    body=body,
    model_id=model_id,
    accept="application/json",
    content_type="application/json"
)

response_body=json.load(response.get("body").read())

response_text=response_body["generation"]
print(response_text)
