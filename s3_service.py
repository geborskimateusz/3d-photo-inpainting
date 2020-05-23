import boto3
from app import app

s3 = boto3.client(
    "s3",
    aws_access_key_id=app.config['S3_KEY'],
    aws_secret_access_key=app.config['S3_SECRET']
)


def upload_file(userid, file_name, bucket):
    
    # Create directory for each image.
    image_dir = file_name[:-3]
    object_name = userid + "/" + image_dir + "/image/" + file_name

    s3_client = boto3.client('s3')
    response = s3_client.upload_file(file_name, bucket, object_name)
    return response
