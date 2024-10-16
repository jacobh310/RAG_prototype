import os
import json
from pinecone import Pinecone, ServerlessSpec
import sagemaker
import yaml
from typing import List
import boto3
import numpy as np
from dotenv import load_dotenv, find_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

with open("..\\..\\configs\\rag.yaml") as f:
    cfg = yaml.load(f, Loader=yaml.FullLoader)

EMB_ENDPOINT_NAME= cfg['EMB_ENDPOINT_NAME']
LLM_ENDPOINT_NAME= cfg['LLM_ENDPOINT_NAME']


iam = boto3.client('iam')
role = iam.get_role(RoleName='SageMakerExecutionRag')['Role']['Arn']

sagemaker_runtime = boto3.client('sagemaker-runtime')


class Rag:

    def __init__(self,
                 embed_model_endpoint_name,
                 llm_model_endpoint_name
                 ) -> None:
        self.embed_model_endpoint_name = embed_model_endpoint_name
        self.llm_model_endpoint_name = llm_model_endpoint_name

    def _invoke_embed_model(self,
                           strings: List):
    
        payload = {
        "inputs": strings }

        payload = json.dumps(payload)

        response = sagemaker_runtime.invoke_endpoint(
            EndpointName=self.embed_model_endpoint_name,
            ContentType='application/json',
            Accept='application/json',
            Body=payload
        )

        response_body = response['Body'].read()
        result = json.loads(response_body)

        return result 
    
        
if __name__  == "__main__":
    
    rag = Rag(EMB_ENDPOINT_NAME,
              LLM_ENDPOINT_NAME)
    
    strings = ["some text here", "some more text goes here too"]
    vector = rag._invoke_embed_model(strings=strings)

    print(len(vector[0][0]))