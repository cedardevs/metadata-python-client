from transform import eventHandler


def test_handler_process():

    body = '{ "Records": ' \
                '   [ ' \
                '     { "eventVersion": "2.1", ' \
                '       "eventSource": "aws:s3",' \
                '       "awsRegion": "us-east-1",' \
                '       "eventTime": "2020-11-10T00:44:20.642Z",' \
                '       "eventName": "ObjectCreated:Put",' \
                '       "userIdentity": {"principalId": "AWS:AIDAUDW4MV7I5RW5LQJIO"},' \
                '       "requestParameters": {"sourceIPAddress": "65.113.158.185"},' \
                '       "responseElements": {"x-amz-request-id": "7D394F43C682BB87",' \
                '       "x-amz-id-2": "k2Yn5BGg7DM5fIEAnwv5RloBFLYERjGRG3mT+JsPbdX033USr0eNObqkHiw3m3x+BQ17DD4C0ErB/VdhYt2Az01LJ4mQ/aqS"},' \
                '       "s3": {"s3SchemaVersion": "1.0", "configurationId": "csbS3notification",' \
                '         "bucket": {"name": "nesdis-ncei-csb-dev",' \
                '           "ownerIdentity": {"principalId": "A3PGJENIF5D10L"},' \
                '           "arn": "arn:aws:s3:::noaa-nesdis-ncei-csb"},' \
                '         "object": {"key": "noaa/nesdis/ncei/csb/csv/file1.csv", "size": 1385,' \
                '           "eTag": "44d2452e8bc2c8013e9c673086fbab7a",' \
                '           "versionId": "q6ls_7mhqUbfMsoYiQSiADnHBZQ3Fbzf",' \
                '           "sequencer": "005FA9E26498815778"}' \
                '       }' \
                '     }' \
                '   ]' \
                '}'

    event = {"Records": [{"body": body}]}

    assert eventHandler.process(event, None) == \
           {'body': '{"message": "Go Archive Team! Your function executed successfully!", '
                    '"evt_name": "ObjectCreated:Put", '
                    '"s3_key": "noaa/nesdis/ncei/csb/csv/file1.csv"}'

               , 'statusCode': 200 }