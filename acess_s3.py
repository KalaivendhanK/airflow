import boto3
import numpy as np

s3=boto3.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)

my_s3_bucket='sample-s3-bucket-for-me'
data=open('upload_to_s3_test_file.txt','rb')
s3.Bucket(my_bucket).put_object(Key='upload_to_s3_test_file.txt',Body=data)
