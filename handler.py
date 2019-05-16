import subprocess
import sys
import json

counter = 0

def handler(event, context):
    global counter
    f = open("/tmp/counter.txt","w+")
    f.writelines("counter: {}".format(counter))
    f.close()
    counter = counter + 1
    if 'tmpfile' in event['body']:
        output = subprocess.check_output("cat /tmp/{}".format(json.loads(event['body'])['tmpfile']), stderr=subprocess.STDOUT, shell=True)
        return {"statusCode": 200, "body": json.dumps(str(output))}
    return None
