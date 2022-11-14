import boto3 
import json
import pandas

# Load Data Into DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('futures')

# Get SOYA Data from DynamoDB
SOYA_JSON = table.get_item(
    Key={
         "instrument_ID": "SOYA"
    }
)

# Store SOYA JSON Data in a Variable
SOYA_PRICES = []
for i in range(0, 7):
    SOYA_PRICES.append(SOYA_JSON['Item']['price' + str(i+1)])

# Convert Strings in Price List into doubles
SOYA_PRICES = [float(i) for i in SOYA_PRICES]