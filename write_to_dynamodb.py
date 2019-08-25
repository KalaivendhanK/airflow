import requests
import random
import string
# Below TODO to read the file contents and dynamically create body for post requests
# It is now hardcoded to test body data
# with open(file,rb) as f:


def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

url='https://k8wpr90m9d.execute-api.ap-south-1.amazonaws.com/dev/res1'
body={
    "name": randomString(5),
    "age":23,
    "qualification": randomString(8)
}
headers = {'content-type': 'application/json'}

try:
    data=requests.post(url=url,json=body,headers=headers)
    print("Post Request Successfull...\n{}".format(data.text))
except:
    print("Requesting the AWS API Gateway endpoint filed with status...\n{}".format(data.text))