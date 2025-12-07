# dictionay is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.

# mention global variables
Sudo="sudo"

# create a dictionary
aws_instance_info = {
    "name" : "webserver",
    "os" : "ubuntu-linux",
    "image" : "ami-28075n99949328",
    "az" : "ap-south-1",
    "tags" : {
        "server" : "test",
        "env" : "testing"
    },
    "subnet" : "subnet-a",
    "vpc" : "my-testvpc",
    "ebs" : {
        "type" : "gp2",
        "memory" : "16gb"
    },
    "script" : {
        "install-server" : "f{Sudo} yum install nginx -y\n service nginx start\n service nginx enabled\n"
    }
}

# Access the above dictionary elements
# get (returns None if key not found)
value = aws_instance_info.get("name")
print(value)

# Access the items
item = aws_instance_info.items()
print(item)
print("\n")

# Access the keys
keys = aws_instance_info.keys()
print(keys)
print("\n")

# Access the values
values = aws_instance_info.values()
print(values)

# len of dictionary
length = len(aws_instance_info)
print(f"\nlength : {length}")

# copy the dictionary
copy = aws_instance_info.copy()
print(f"\nCopy the dictionary : \n\t{copy}")

# clear the dictionary
aws_instance_info.clear()
print(aws_instance_info)
