import json
import requests
from config import base_url

def lambda_handler(event, context):
    res = requests.get(url=base_url + 'todos/1')
    return {
        'statusCode': res.status_code,
        'body': json.dumps(res.json())
    }
