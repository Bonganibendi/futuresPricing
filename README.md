# South African Grain Future Prices 

![Screenshot 2022-11-25 at 14 06 21](https://user-images.githubusercontent.com/58882596/203982916-a8304712-8a99-46f2-8642-5ce1ce0e6518.png)

An app which uses AWS Serverless computing to scrape South African Futures Grain Prices. The data is then parsed into an easy to view desktop application to monitor the current prices for the future contracts. 

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

# How to Setup 

- Zip the packages in one file.
- Create a DynamoDB table corresponding with the data which is being scrapped.
- Create an IAM role in your AWS Management Console to allow a Lambda function to read and write data from your DynamoDB table.
- Create a Lambda function and assign the role.
- Add the zipped file with the create packages in the layers of the function. 
- Create an Eventbridge to automate the Lambda function to scrape daily.
- Install AWS CLI Tools on the Desktop Environment where you will run the application and configure it to the same VPC as your DynamoDB and Lambda function.
- Run the app. 
