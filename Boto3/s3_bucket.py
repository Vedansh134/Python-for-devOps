import boto3

# botocore - kind of module that have all exception
#resource = boto3.resource("ec2")

client = boto3.client("s3")

response = client.create_bucket(
    ACL='private',
    Bucket='vedansh-kumar-134-bucket',
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1',
        'Tags': [
            {
                'Key': 'region',
                'Value': 'mumbai'
            },
        ]
    },
    ObjectLockEnabledForBucket=True,
    ObjectOwnership='BucketOwnerPreferred'
)

response = client.get_bucket_acl(
    Bucket='vedansh-kumar-134-bucket'
)
print(response)