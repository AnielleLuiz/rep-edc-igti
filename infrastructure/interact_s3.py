import boto3
import pandas as pd

s3_client = boto3.resource(
    service_name='s3',
    region_name='us-east-1',
    aws_access_key_id='AKIAXCOULJ5TYFP52VEM',
    aws_secret_access_key='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'   
)

import os
os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'
os.environ['AWS_ACCESS_KEY_ID'] = 'AKIAXCOULJ5TYFP52VEM'
os.environ['AWS_SECRET_ACCESS_KEY'] = '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'

#s3_client.meta.client.download_file('dl-igti-edc-anielle', 'data/dados_pedidos.csv', 'c:\\data\\dados_pedidos.csv')

#df = pd.read_csv('dados_pedidos.csv', sep=',')
#print(df)

s3_client.meta.client.upload_file('c:\\data\\hello.txt', 'dl-igti-edc-anielle', 'data/hello.txt')