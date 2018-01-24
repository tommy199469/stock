import boto3 , botocore, s3_config
import pandas as pd


def upload_file(file_name):
    # Create an S3 client
    s3  = boto3.resource(
        's3',
        aws_access_key_id=s3_config.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=s3_config.AWS_SECRET_ACCESS_KEY,
        region_name=s3_config.AWS_DEFAULT_REGION
    )
    object_acl = s3.ObjectAcl(s3_config.BUCKET_NAME,file_name)
    response = object_acl.put(ACL='public-read')
    return response

def download_file():
    s3  = boto3.resource(
        's3',
        aws_access_key_id=s3_config.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=s3_config.AWS_SECRET_ACCESS_KEY,
        region_name=s3_config.AWS_DEFAULT_REGION
    )

    try:
        s3.Bucket(s3_config.BUCKET_NAME).download_file("stock.xlsx", 'stock.xlsx')
    except botocore.exceptions.ClientError as e:
        return False

    return True
