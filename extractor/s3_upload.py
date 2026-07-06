import boto3
import json
from config import (
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
    AWS_REGION,
    S3_BUCKET_NAME
)

s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

def upload_json(data, object_key):
    """
    Upload JSON data directly to S3
    """

    s3.put_object(
        Bucket=S3_BUCKET_NAME,
        Key=object_key,
        Body=json.dumps(data, indent=4),
        ContentType="application/json"
    )

    print(f"Uploaded to s3://{S3_BUCKET_NAME}/{object_key}")