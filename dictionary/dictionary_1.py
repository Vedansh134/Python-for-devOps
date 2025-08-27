# dictionary is also a data-type which store data in key-value pair (JSON FOMRAT)
# used to show complete propeties of that like ec2
# key : value pairs

aws_instance_info = {
    "name" : "server",
    "id" : "564788cfgr6699",
    "type" : "t2.micro",
    "OS" : "ubuntu",
    "storage" : {
        "type" : "gp2",
        "size" : "30GB"
    },
    "secruity-grps" : [22,443],
    "script" : "apt update\n sudo apt install docker.io -y\n",
    "a" : (1,2,3)
}

try:
    print(aws_instance_info.values())
except KeyError:
    print("error")
except TypeError:
    print("give values() not only dict name")

# get (return values)
value = aws_instance_info.get("a")
print(f"values : {value}")

# all itms


