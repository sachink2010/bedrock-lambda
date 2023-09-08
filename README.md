# bedrock-lambda
Lambda function to access Amazon Bedrock
This is a sample Lambda function to access Amazon Bedrock.

Pre-requisites ofr using this is that you need to have Amazon Bedrock available in your AWS Account.

Steps to make it work:
1. Create a Basic Lambda function Python 3.11:
Author from scratch, Give unction name, Runtime-Python 3.11, Architecture-x86_64, permissions as default to start with. Hit create function
2. Add Bedrock Permissions to Lambda:
Once Lambda function is created, go to Configuration-->Permission--RoleName(click on role link)-->Permissions-->Add Permissions-->create Inline policy-->Search for Bedrock-->Select Bedrock-->Add All Actions-->All resources-->give policy name-->create policy
3. Set Time-out for Lambda to say 1 min: Sometimes it takes time to execute. You can do this in Lambda-->Configuration-->General Configuration
4. Upload Lambda Layers zip file to S3: Download zip file from github repo-->almbda layers folder and upload it to S3 in your bucket (same region as Bedrock)
5. Create a layer for Bedrock: 
Go to Lambda Screen. Go to left menu-->Additionla resources-->Layers-->create Layer-->upload from S3-->Give path of step 4, compatible runtime as Python 3.11-->Create
6. Add Custom Layer to Lambda: Add layer created in step 5 into Lambda function, using front-end. Open Lambda function-->Click layers-->Add layer-->custom layer-->Select layer from step 5
7. Copy code from lambda_code/lambda_function.py to your lambda function code

It should all work now!

   
   
