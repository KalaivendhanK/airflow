import requests

# Below TODO to read the file contents and dynamically create body for post requests
# It is now hardcoded to test body data
# with open(file,rb) as f:

url='https://k8wpr90m9d.execute-api.ap-south-1.amazonaws.com/dev/res1'
body={
    "name": "test_name",
    "age":23,
    "qualification": "test_qualification"
}
headers = {'content-type': 'application/json'}

try:
    data=requests.post(url=url,json=body,headers=headers)
    print("Post Request Successfull...\n{}".format(data.text))
except:
    print("Requesting the AWS API Gateway endpoint filed with status...\n{}".format(data.text))