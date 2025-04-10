import boto3
import linux

# Create an EC2 client using the default region from AWS CLI configuration
ec2 = boto3.client('ec2')
#Adding a line to my developer branch
# Launch an EC2 instance
response = ec2.run_instances(
    ImageId='ami-08cb53946b34ef980',  # Amazon Linux 2 AMI (Free tier eligible, update as needed)
    InstanceType='t3.micro',
    KeyName='boto3-key',  # Ensure this key pair exists in your AWS account
    MinCount=1,
    DesiredCount=1,
    MaxCount=1
)
