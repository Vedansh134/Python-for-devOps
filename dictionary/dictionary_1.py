# dictionary is also a data-type which store data in key-value pair (JSON FOMRAT)
# used to show complete propeties of that like ec2
# key : value pairs

aws_instance_info = {
    "name" : "web-server",
    "id" : "564788cfgr6699",
    "type" : "t2.micro",
    "OS" : "ubuntu",
    "storage" : {
        "type" : "gp2",
        "size" : "30GB"
    },
    "security-groups" : [22,443],
    "script" : "\n\tapt update\n\tsudo apt install docker.io -y\n",
    "a" : (1,2,3)
}

try:
    print(aws_instance_info.values())
except KeyError:
    print("error")
except TypeError:
    print("give values() not only dict name")


# get values
val = aws_instance_info.get("name")
print(val)

# Access keys
keys = aws_instance_info.keys()
print(keys)

# length of dictionary
length = len(aws_instance_info)
print(length)

# Access dictionary keys and values
for key in range(length):
    print(f"{key} keys : {list(aws_instance_info.keys())[key]} and values : {list(aws_instance_info.values())[key]}")

# Update the value
aws_instance_info["type"] = "t3.4Xlarge"
print(aws_instance_info)

# Extend
new_feat = {
    "eip" : "yes"
}
aws_instance_info.update(new_feat)
print(aws_instance_info)
