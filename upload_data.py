import boto3
import time
from Xlib import display
import datetime
import json

KEY_ID = ""
SECRET_KEY = ""
REGION = ""
STREAM_NAME = ''

kinesis_client = boto3.client('kinesis',
                              aws_access_key_id=KEY_ID,
                              aws_secret_access_key=SECRET_KEY,
                              region_name=REGION
                              )
first_id = 0
while True:
    qp = display.Display().screen().root.query_pointer()
    item = {}
    item['@timestamp'] = str(datetime.datetime.now())
    item['user'] = 'edan'
    item['x'] = qp.root_x
    item['y'] = qp.root_y

    put_response = kinesis_client.put_record(
        StreamName=STREAM_NAME,
        Data=json.dumps(item),
        PartitionKey='aa-bb')
    print(item)


