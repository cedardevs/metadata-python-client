import json


class Granule:

    payload = {}

    def __init__(self):
        self.payload["CollectionReference"] = {"ShortName": "CollectionShortName", "Version": "1.6"}
        self.payload["MetadataSpecification"] = {"URL": "CollectionShortName", "Name": "UMM-G", "Version": "1.6"}

    def serialize(self):

        json_payload = json.dumps( self.payload, indent=2 )

        # Return
        return json_payload
