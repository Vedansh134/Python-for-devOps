# Start practicing Python for DevOps
print("Hello world from python \nLet's start practicing Python for DevOps")

## This is a single line comment

# -----------------------------
# Different methods in string
# -----------------------------

# Concatenation in string
str1 = "ap-south-1.console"
str2 = ".aws.amazon.com"

final_str=str1+str2
print(f"AWS URL : {final_str}")


# lower and upper case
print(final_str.upper())
print(final_str.lower())


# slicing : make a substring
sub_string = final_str[0:10]
print(f"Slicing : {sub_string}")


# split : break string 
bucket_url = "https://test-bucket.s3.ap-south-1://67uuu9"

break1 = bucket_url.split(":")
print(break1)
print(break1[1])

# task : print only bucket name - use split
s3_url = "https://test-bucket.s3.ap-south-1://67uuu9"
bucket_name = s3_url[8:19]
print(f"Bucket name : {bucket_name}")


# Replacing a string
replace_url = s3_url.replace("s3","ec2")
print(f"Replace url : {replace_url}")


# Remove strips
cloud = "  'AWS'  "
print(f"Original test : {cloud}")

strip = cloud.strip()
print(f"Stripped : {strip}")

left_strip = cloud.lstrip()
print(f"left side stripped : {left_strip}")

right_strip = cloud.rstrip()
print(f"right side stripped : {right_strip}")

# doubt : print(f"right side stripped : {cloud.rstrip()}")

# find method
ec2_info = "t2.micro instance in us-east-1"
position = ec2_info.find("us-east-1")
print(f"Location : {position}")

# for practice and learning purpose change/add code : hard-reset
print("hard reset and other change in vscode for raise intentionally conflict issue")

