import json
from jsonschema import validate
import unittest
from cmr.info.Granule import Granule


class GranuleTest(unittest.TestCase):
    schema = None

    def setUp(self):
        with open("../schemas/granule/v1.6.2/umm-g-json-schema.json") as file:
            self.granule_schema = json.load(file)
        with open("../schemas/collection/v1.16.2/umm-cmn-json-schema.json") as file:
            self.collection_schema = json.load(file)

    def test_dynamic_granule_payload(self):
        granule = Granule()
        granule.payload["GranuleUR"] = "OISST_Unique_Granule_v1.6.2"
        granule.payload["ProviderDates"] = [{"Date": "2021-04-28T00:00:00Z"}, {"Type": "Create"}]
        payload = granule.serialize()
        print("\n" + payload)
        # If no exception is raised by validate(), the instance is valid.
        validate(instance=payload, schema=self.granule_schema)

    assert eventHandler.process( event, None ) == \
           {'body': '{"message": "Go Archive Team! Your function executed successfully!", '
                    '"payload": "ObjectCreated:Put", '
                    '"s3_key": "noaa/nesdis/ncei/csb/csv/file1.csv"}'

               , 'statusCode': 200 }
