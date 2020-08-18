import json

def lambda_handler(event, _):
    return handle_rest(event, handle_get, handle_post)

def handle_rest(event, get, post):
    if event.get("httpMethod") is not None:
        if event.get("httpMethod") == "GET":
            return handle_get()
        elif event.get("httpMethod") == "POST":
            return handle_post(event.get("body"))

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
    return {
        'statusCode': 201,
        'body': json.dumps(data)
    }