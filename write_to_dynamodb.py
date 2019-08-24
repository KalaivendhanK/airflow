import requests

url='https://k8wpr90m9d.execute-api.ap-south-1.amazonaws.com/dev/res1'
params={
    "name": "test_name",
    "age":23,
    "qualification": "test_qualification"
}

requests.post(url=url,params=params)