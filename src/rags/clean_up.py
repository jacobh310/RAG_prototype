import boto3
import yaml

session = boto3.Session()
sagemaker = session.client('sagemaker')


with open("..\\..\\configs\\rag.yaml") as f:
    cfg = yaml.load(f, Loader=yaml.FullLoader)

EMB_ENDPOINT_NAME= cfg['EMB_ENDPOINT_NAME']
EMB_MODEL_NAME =cfg['EMB_MODEL_NAME']
LLM_ENDPOINT_NAME= cfg['LLM_ENDPOINT_NAME']
LLM_MODEL_NAME = cfg['LLM_MODEL_NAME']


sagemaker.delete_endpoint(EndpointName=LLM_ENDPOINT_NAME)
sagemaker.delete_model(ModelName=LLM_MODEL_NAME)
sagemaker.delete_endpoint_config(EndpointConfigName=LLM_ENDPOINT_NAME)

sagemaker.delete_endpoint(EndpointName=EMB_ENDPOINT_NAME)
sagemaker.delete_model(ModelName=EMB_MODEL_NAME)
sagemaker.delete_endpoint_config(EndpointConfigName=EMB_ENDPOINT_NAME)


print("Endpoints Successfully Deleted")