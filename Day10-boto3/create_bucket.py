import boto3

s3 = boto3.client('s3')

bucket_name = "scott-boto3-demo-bucket"

try:
    s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={"LocationConstraint": "ap-southeast-2"}  # 你的 Region
    )
    print(f"✅ Created bucket: {bucket_name}")
except Exception as e:
    print(f"❌ Error: {e}")
