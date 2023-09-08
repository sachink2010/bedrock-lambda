import boto3
import json

modelId = 'anthropic.claude-v2' 
accept = 'application/json'
contentType = 'application/json'

instruction = "Human: Write an essay based on the the question " # If you don't know the answer, just say that you don't know, don't try to make up an answer."


def lambda_handler(event, context):
    

    bedrock = boto3.client(service_name='bedrock',
                       region_name='us-east-1',
                       endpoint_url='https://bedrock.us-east-1.amazonaws.com')
    retval = ""
    question="write an essay for living on mars in 1000 words"
    prompt = instruction + "\n" + "Context: " +  "\n" + "Question: " + question + "\n Assistant:"
    body = json.dumps({
            "prompt":prompt,
            "max_tokens_to_sample":2048,
            "temperature":0,
            "top_k":250,
            "top_p":1,
            "stop_sequences":["\n\nHuman:"]
        })
    response = bedrock.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)
    response_body = json.loads(response.get('body').read())
    retval = response_body["completion"]
        
    return {
        'statusCode': 200,
        'body': json.dumps(retval)
    }