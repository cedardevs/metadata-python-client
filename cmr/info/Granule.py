import json


class Granule:

    payload = {}

    def __init__(self):
        self.payload["CollectionReference"] = {"ShortName": "CollectionShortName", "Version": "1.6.2"}
        self.payload["MetadataSpecification"] = {"URL": "https://cdn.earthdata.nasa.gov/umm/granule/v1.6.2", "Name": "UMM-G", "Version": "1.6.2"}

    def serialize(self):

        json_payload = json.dumps(self.payload)

        # Return
        return json_payload
