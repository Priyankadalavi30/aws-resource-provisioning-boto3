import boto3

# S3 client create
s3 = boto3.client(
    's3',
    region_name='ap-south-1'
)

# Unique bucket name
bucket_name = 'priyanka-demo-bucket-2026-001'

# Create S3 bucket
s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'
    }
)

print(f"Bucket '{bucket_name}' created successfully!")