from io import BytesIO
import logging
import json
import joblib
import boto3


# logger class
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# HELPER function to download from s3


def GetDataFromS3(bucket, key):
    s3 = boto3.client('s3')
    with BytesIO() as f:
        s3.download_fileobj(Bucket=bucket, Key=key, Fileobj=f)
        f.seek(0)
        test_features = joblib.load(f)
    return test_features


logger.info('loading model from file....')
model = joblib.load('models/knn_model.joblib')
logger.info('model loaded from file ...')


def lambda_handler(event, context):
    # read json packet
    data = json.loads(event['body'])
    bucket = data['bucket']
    key = data['key']
    # load data from s3
    logger.info('load data from s3')
    test_features = GetDataFromS3(bucket, key)
    logger.info(f'loaded {type(key)} from s3...')
    logger.info('performing predictions...')
    predictions = model.predict(test_features)
    response = json.dumps(predictions.tolist())  
    return {
        'statusCode': 200,
        'headers': {
            'Content-type': 'application/json'
        },
        'body': response
    }
