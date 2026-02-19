# List in python

# AWS Regions
regions = ["ap-south-1",["ap-south-1a, ap-south-1b"],"ap-south-2","ap-north-1"]

# AWS Services
aws_services = ["EC2", "S3", "Lambda", "RDS", "DynamoDB", "VPC"]


# -----------------------------------------------------------------------
# ------------- Adding operation ------------


# ---- Append operation
aws_services.append("ECR")
aws_services.append("EKS")

print(f"appending {aws_services}")

# ------ Nested list appending
regions[1].append("ap-south-1c")
print(regions)


# ---- Insert ( at specific )
aws_services.insert(1,"EBS")


# ---- Extend
devops = ["ecr","ecs","eks","codecommit","codebuild","codedeploy"]
aws_services.extend(devops)
print(aws_services)



# ---------------------------------------------------------------------------
# ------------------- removing operation ------------------------


active_resources = ["EC2", "S3", "Lambda", "RDS", "DynamoDB"]

# ---- Remove 
active_resources.remove("EC2")
print(active_resources)

# ---- Pop ( spcific index or from last)
active_resources.pop(3)
print(active_resources)


# -----------------------------------------------------------------------------
# --------------------- finding operation ----------------------

instance_types = ["t2.micro", "t3.medium", "m5.large", "t2.micro", "c5.xlarge"]

finder = instance_types.index("t2.micro")
print(finder) # give index - 0

count = instance_types.count("t2.micro")
print(f"The no. of ec2 : {count}")