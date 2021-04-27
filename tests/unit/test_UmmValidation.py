import json
from jsonschema import validate
import unittest


class UmmValidation(unittest.TestCase):
    schema = None

    def setUp(self):
        with open("../schemas/granule/v1.6.2/umm-g-json-schema.json") as file:
            self.granule_schema = json.load(file)
        with open("../schemas/collection/v1.16.2/umm-cmn-json-schema.json") as file:
            self.collection_schema = json.load(file)

    def test_granule_payload(self):
        payload = \
            {
                "GranuleUR": "Unique_Granule_UR_v1.6",
                "ProviderDates": [
                    {"Date": "2018-07-19T00:00:00Z",
                     "Type": "Create"}
                ],
                "CollectionReference": {
                    "ShortName": "CollectionShortName",
                    "Version": "1.6"
                },
                "MetadataSpecification": {
                    "URL": "https://cdn.earthdata.nasa.gov/umm/granule/v1.6.2",
                    "Name": "UMM-G",
                    "Version": "1.6.2"
                }
            }
        # If no exception is raised by validate(), the instance is valid.
        validate(instance=payload, schema=self.granule_schema)

    def test_granule_example(self):
        with open("../schemas/granule/v1.6.2/GranuleExample.json") as file:
            payload = json.load(file)
        validate(instance=payload, schema=self.granule_schema)

    def test_granule_example1(self):
        with open("../schemas/granule/v1.6.2/GranuleExample1.json") as file:
            payload = json.load(file)
        validate(instance=payload, schema=self.granule_schema)

    def test_collection_example(self):
        with open("../schemas/granule/v1.6.2/CollectionExample.json") as file:
            payload = json.load(file)
        validate(instance=payload, schema=self.collection_schema)

    def test_collection1_example(self):
        with open("../schemas/granule/v1.6.2/CollectionExample1.json") as file:
            payload = json.load(file)
        validate(instance=payload, schema=self.collection_schema)
