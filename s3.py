import boto3 , botocore, s3_config


# Create an S3 client
s3  = boto3.resource(
    's3',
    aws_access_key_id=s3_config.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=s3_config.AWS_SECRET_ACCESS_KEY,
    region_name=s3_config.AWS_DEFAULT_REGION
)




#download 
"""try:
    s3.Bucket(s3_config.BUCKET_NAME).download_file("stock.xlsx", 'stock.xlsx')
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise
"""
