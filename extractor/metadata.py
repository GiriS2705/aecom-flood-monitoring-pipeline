import json
import boto3
from botocore.exceptions import ClientError
from config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION
from datetime import datetime, UTC


BUCKET_NAME = "aecompipeline"
METADATA_KEY = "flood-monitoring/metadata/pipeline_metadata.json"

s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)


def get_last_successful_load():
    try:
        response = s3.get_object(
            Bucket=BUCKET_NAME,
            Key=METADATA_KEY
        )

        metadata = json.loads(response["Body"].read().decode())

        # return metadata["last_successful_load"]
        return metadata["last_successful_load"][:10]

    except ClientError:

        # First pipeline execution
        return "2026-07-01"


def update_last_successful_load():

    metadata = {
        "pipeline_name": "flood_monitoring_pipeline",
        "last_successful_load": datetime.now(UTC).isoformat()
    }

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=METADATA_KEY,
        Body=json.dumps(metadata, indent=4),
        ContentType="application/json"
    )