import boto3
import json

def lambda_handler(event, context):
    client = boto3.client('sagemaker', region_name="us-west-2")

    response = client.create_presigned_domain_url(
        DomainId='d-8fqk644ntygk',
        UserProfileName='prabhat',
        SessionExpirationDurationInSeconds=43200,
        ExpiresInSeconds=5
    )

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps(response)
    }
