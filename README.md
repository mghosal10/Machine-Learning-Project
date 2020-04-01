# Classification-Project

# Project Aim 
Train a document classification model and deploy the model to a public cloud platform as a webservice.

# Deployment Steps

1. Set up an AWS account on https://aws.amazon.com/
2. Create an EC2 instance and select Ubuntu
3. Launch the instance and keep save the key-pair.pem safely
4. Connect to your EC2 instance using Terminal
   a) sudo chown -v username key-pait.pem
   b) chmod 400 key-pair.pem   
   c) ssh -i key-pair.pem ubuntu@http://ec2-3-134-94-20.us-east-2.compute.amazonaws.com/
5. Upload all the files to the EC2 instance using FileZilla/Putty
6. Navigate to the project directory in the EC2 instance and run webservice.py

The project can be tested at http://ec2-3-134-94-20.us-east-2.compute.amazonaws.com:5000/


