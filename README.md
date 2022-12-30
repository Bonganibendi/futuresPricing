![Screenshot 2022-12-30 at 13 51 17](https://user-images.githubusercontent.com/58882596/210068895-5c9a45b6-60a7-456d-8583-4a2a4a5d6c33.png)

# South African Grain Future Prices 

An app which uses AWS Serverless computing to scrape South African Futures Grain Prices. The data is then parsed into an easy to view desktop application to monitor the current prices for future contracts. 

# Skills Acquired from Project 

- AWS Lambda and the basic principles of serverless computing.
- Layers in AWS lambda to use python libraries. 
- AWS DynamoDB database for storing futures prices.
- AWS SDK and BOTO3 for Infrastructure as Code.
- Web Scraping using BeautifulSoup4.
- DearPyGui a C++ GUI library wrapped in Python to make my desktop application. 
- AWS CLI Tools.
- Automating my Lambda using AWS EventBridge.
- Creating an Architecture of the AWS Services most effective for this project.

# Architecture Diagram

![Untitled](https://user-images.githubusercontent.com/58882596/204089888-c018d33a-9b30-4fb1-b0db-6f00f452a48a.png)

# How to Setup 

- Download the packages imported on all of the script files.
- Download the many Linux x86_64 .whl version of the python packages for the scraping_script.py.
- Zip the packages in one file.
- Create a DynamoDB table corresponding with the data which is being scrapped.
- Create an IAM role in your AWS Management Console to allow a Lambda function to read and write data from your DynamoDB table.
- Create a Lambda function and assign the role.
- Add the zipped file with the create packages in the layers of the function. 
- Create an Eventbridge to automate the Lambda function to scrape daily.
- Install AWS CLI Tools on the Desktop Environment where you will run the application and configure it to the same VPC as your DynamoDB and Lambda function.
- Run the app. 
