import boto3

def ok(label, data):
    print("[OK]", label, data)

def warn(label, err):
    print("[WARN]", label, err)

try:
    AWS_management_console = boto3.session.Session(profile_name='default')
    ok("Session Created", (AWS_management_console.region_name or 'default', AWS_management_console.profile_name or 'default'))
except Exception as e:
    warn("Session Creation", e)

# STS
try:
    sts = AWS_management_console.client("sts")
    ident = sts.get_caller_identity()
    ok("STS Identity", ident)
except Exception as e:
    warn("STS Identity", e)

# S3
try:
    s3 = AWS_management_console.client("s3")
    buckets = s3.list_buckets().get("Buckets", [])
    ok("S3 Buckets", [b["Name"] for b in buckets])
except Exception as e:
    warn("S3 Buckets", e)

# EC2
try:
    ec2 = AWS_management_console.client("ec2")
    res = ec2.describe_instances()
    instance_ids = [i["InstanceId"] for r in res["Reservations"] for i in r["Instances"]]
    ok("EC2 Instances", instance_ids)
except Exception as e:
    warn("EC2 Instances", e)

# CloudWatch
try:
    cw = AWS_management_console.client("cloudwatch")
    alarms = cw.describe_alarms(MaxRecords=20).get("MetricAlarms", [])
    ok("CloudWatch Alarms", [a["AlarmName"] for a in alarms])
except Exception as e:
    warn("CloudWatch Alarms", e)
