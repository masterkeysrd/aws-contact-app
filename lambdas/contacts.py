import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Contact')

def lambda_handler(event, _):
    return handle_rest(event, handle_get, handle_post)

def handle_rest(event, get_fun, post_fun):
    if event.get("httpMethod") is not None:
        if event.get("httpMethod") == "GET":
            return get_fun()
        elif event.get("httpMethod") == "POST":
            return post_fun(event.get("body"))

def handle_get():
    contacts = [
        {
            "name": "David Morales",
            "phone": "809-121-2312",
            "email": "morales.david1997@gmail.com"
        },
        {
            "name": "John Smit",
            "phone": "809-222-2312",
            "email": "jsmit@gmail.com"
        }
    ]
    return {
        'statusCode': 200,
        'body': json.dumps(contacts)
    }


def handle_post(data):
    table.put_item(
        Item=json.loads(data)
    )
    return {
        'statusCode': 201,
        'body': json.dumps(data)
    }