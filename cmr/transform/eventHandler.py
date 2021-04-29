import json
from cmr.info.Granule import Granule

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

        # "GranuleUR": "OISST_Unique_Granule_v1.6.2",
        # "ProviderDates": [{
        #     "Date": "2021-04-28T00:00:00Z",
        #     "Type": "Create"
        # }]

        granule = Granule()
        granule.payload["GranuleUR"] = "OISST_Unique_Granule_v1.6.2"
        granule.payload["ProviderDates"] = {"Date": "2021-04-28T00:00:00Z", "Type": "Create"}


    body = granule.serialize()

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
