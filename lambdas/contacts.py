import json

def lambda_handler(event, _):
    return {
        'statusCode': 200,
        'body': json.dump("Hello from Lambda!!!")
    }