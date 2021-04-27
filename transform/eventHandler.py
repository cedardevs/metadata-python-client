import json

def process(event, context):
    evt_name: None
    s3_key: None

    for rec in event["Records"]:

        body = rec["body"]

        msg = json.loads(body)

        recs = msg["Records"]

        rec = recs[0]  # This is standard format 1 record per message for now according to AWS docs

        evt_name = rec.get("eventName")
        s3_key = rec.get("s3").get("object").get("key")
        print(s3_key)

    body = {
        "message": "Go Archive Team! Your function executed successfully!",
        "evt_name": evt_name,
        "s3_key": s3_key
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response
