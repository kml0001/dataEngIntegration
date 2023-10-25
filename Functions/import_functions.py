import json
import boto3


def from_json_s3(bucket, partition):
    s3 = boto3.client("s3")
    response = s3.get_object(Bucket=bucket, Key=partition)

    # via 1
    json_file = json.loads(response["Body"])

    # via 2
    # json_file = response["Body"].read().decode("utf-8")
    # json_file = json.loads(json_file)

    return json_file


def from_json(path):
    with open(path, "r") as file:
        json_file = json.load(file)

    return json_file
