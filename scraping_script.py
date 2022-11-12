# Imports
from bs4 import BeautifulSoup
import requests
import pandas as pd
import boto3

# Initialisation
url = "https://www.grainsa.co.za/pages/industry-reports/safex-feeds"
# create url object
page = requests.get(url)
soup = BeautifulSoup(page.text, "lxml")

# Getting Table
table = soup.find("table", {"class":"table table-striped table-bordered"})

# Remove first row in table
table.find("tr").decompose()

# Getting Headers
headers = []

for i in table.find_all("th"):
    title = i.text.strip()
    headers.append(title)

# Create Columns with Headers
df = pd.DataFrame(columns = headers)

# Getting Rows
for row in table.find_all("tr")[1:]:
    data = row.find_all("td")
    row_data = [td.text.strip() for td in data]
    length = len(df)
    df.loc[length] = row_data

# Keep data of columns of interest
df = df.iloc[:, [0, 1, 3]]


# Split df into multiple tables based on the instruments
SOYA = df[df['Instrument'].str.contains("SOYA")]
SUNS = df[df['Instrument'].str.contains("SUNS")]
WEAT = df[df['Instrument'].str.contains("WEAT")]
WMAZ = df[df['Instrument'].str.contains("WMAZ")]
YMAZ = df[df['Instrument'].str.contains("YMAZ")]

# SOYA Items Into Lists
SOYA_PRICE = SOYA['LastTradedPrice'].tolist()

# SUNS Items Into Lists
SUNS_PRICE = SUNS['LastTradedPrice'].tolist()

# WEAT Items Into Lists
WEAT_PRICE = WEAT['LastTradedPrice'].tolist()

# WMAZ Items Into Lists
WMAZ_PRICE = WMAZ['LastTradedPrice'].tolist()

# YMAZ Items Into Lists
YMAZ_PRICE = YMAZ['LastTradedPrice'].tolist()

# Load Data Into DynamoDB

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('futures')

# Update Expression
table.update_item(
    Key={
        'instrument_ID': 'SOYA',
    },
    UpdateExpression="SET price1 = :val1",
    ExpressionAttributeValues={
        ':val1': 26
    }
)

# Update Price of SOYA Data in DynamoDB using SOYA_PRICE with Update Expression syntax above using a loop 
for i in range(len(SOYA_PRICE)):
    table.update_item(
        Key={
            'instrument_ID': 'SOYA',
        },
        UpdateExpression="SET price" + str(i+1) + " = :val" + str(i+1),
        ExpressionAttributeValues={
            ':val' + str(i+1): SOYA_PRICE[i]
        }
    )

# Update Price of SUNS Data in DynamoDB using SUNS_PRICE with Update Expression syntax above using a loop
for i in range(len(SUNS_PRICE)):
    table.update_item(
        Key={
            'instrument_ID': 'SUNS',
        },
        UpdateExpression="SET price" + str(i+1) + " = :val" + str(i+1),
        ExpressionAttributeValues={
            ':val' + str(i+1): SUNS_PRICE[i]
        }
    )

# Update Price of WEAT Data in DynamoDB using WEAT_PRICE with Update Expression syntax above using a loop
for i in range(len(WEAT_PRICE)):
    table.update_item(
        Key={
            'instrument_ID': 'WEAT',
        },
        UpdateExpression="SET price" + str(i+1) + " = :val" + str(i+1),
        ExpressionAttributeValues={
            ':val' + str(i+1): WEAT_PRICE[i]
        }
    )

# Update Price of WMAZ Data in DynamoDB using WMAZ_PRICE with Update Expression syntax above using a loop
for i in range(len(WMAZ_PRICE)):
    table.update_item(
        Key={
            'instrument_ID': 'WMAZ',
        },
        UpdateExpression="SET price" + str(i+1) + " = :val" + str(i+1),
        ExpressionAttributeValues={
            ':val' + str(i+1): WMAZ_PRICE[i]
        }
    )

# Update Price of YMAZ Data in DynamoDB using YMAZ_PRICE with Update Expression syntax above using a loop
for i in range(len(YMAZ_PRICE)):
    table.update_item(
        Key={
            'instrument_ID': 'YMAZ',
        },
        UpdateExpression="SET price" + str(i+1) + " = :val" + str(i+1),
        ExpressionAttributeValues={
            ':val' + str(i+1): YMAZ_PRICE[i]
        }
    )


