import json


def hello(event, context):
	print("Lambda ran sucessfully")
    body = {
        "message": "Go Serverless v2.0! Your function executed successfully! New version for dev stage",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
