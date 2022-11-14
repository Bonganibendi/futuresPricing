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
for i in range(0, 6):
    SOYA_PRICES.append(SOYA_JSON['Item']['price' + str(i+1)])

# Convert Strings in Price List into doubles
SOYA_PRICES = [float(i) for i in SOYA_PRICES]


# Get SUNS Data from DynamoDB
SUNS_JSON = table.get_item(
    Key={
         "instrument_ID": "SUNS"
    }
)

# Store SUNS JSON Data in a Variable
SUNS_PRICES = []
for i in range(0, 6):
    SUNS_PRICES.append(SUNS_JSON['Item']['price' + str(i+1)])

# Convert Strings in Price List into doubles
SUNS_PRICES = [float(i) for i in SUNS_PRICES]


# Get SUNS Data from DynamoDB
WEAT_JSON = table.get_item(
    Key={
         "instrument_ID": "WEAT"
    }
)

# Store SUNS JSON Data in a Variable
WEAT_PRICES = []
for i in range(0, 6):
    WEAT_PRICES.append(WEAT_JSON['Item']['price' + str(i+1)])

# Convert Strings in Price List into doubles
WEAT_PRICES = [float(i) for i in WEAT_PRICES]

# Get SUNS Data from DynamoDB
WMAZ_JSON = table.get_item(
    Key={
         "instrument_ID": "WMAZ"
    }
)

# Store SUNS JSON Data in a Variable
WMAZ_PRICES = []
for i in range(0, 6):
    WMAZ_PRICES.append(WMAZ_JSON['Item']['price' + str(i+1)])

# Convert Strings in Price List into doubles
WMAZ_PRICES = [float(i) for i in WMAZ_PRICES]

# Get SUNS Data from DynamoDB
YMAZ_JSON = table.get_item(
    Key={
         "instrument_ID": "YMAZ"
    }
)

# Store SUNS JSON Data in a Variable
YMAZ_PRICES = []
for i in range(0, 6):
    YMAZ_PRICES.append(YMAZ_JSON['Item']['price' + str(i+1)])

# Convert Strings in Price List into doubles
YMAZ_PRICES = [float(i) for i in YMAZ_PRICES]