import boto3

# EC2 resource create
ec2 = boto3.resource(
    'ec2',
    region_name='ap-south-1'
)

# Create EC2 instance
instance = ec2.create_instances(
    ImageId='ami-03bb6d83c60fc5f7c',
    MinCount=1,
    MaxCount=1,
    InstanceType='t3.micro'
)

print("EC2 Instance Created Successfully")