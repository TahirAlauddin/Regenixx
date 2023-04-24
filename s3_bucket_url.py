import boto3
import os
import re
from dotenv import load_dotenv
load_dotenv()

AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')



def get_url():
    
    latest_version = get_latest_version() 
    bucket_name = 'regenixx'

    # Create an S3 client
    s3 = boto3.client('s3', region_name='us-east-2', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)


    # Generate a pre-signed URL for the latest version
    presigned_url = s3.generate_presigned_url('get_object', Params={'Bucket': bucket_name, 'Key': latest_version})

    return presigned_url


def get_latest_version():

    # Create an S3 client
    s3 = boto3.client('s3', region_name='us-east-2', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)

    # Set the bucket name and key prefix
    bucket_name = 'regenixx'
    key_prefix = 'regenixx-'

    # List all objects in the bucket
    response = s3.list_objects(Bucket=bucket_name, Prefix=key_prefix)

    # Filter the objects to find the software files
    software_files = [obj['Key'] for obj in response['Contents'] if obj['Key'].startswith(key_prefix) and obj['Key'].endswith('.zip')]

    # Get the latest version of the software
    latest_version = max(software_files, key=lambda f: tuple(map(int, re.search(r'(\d+)\.(\d+)\.(\d+)\.zip', f).groups())))

    return latest_version