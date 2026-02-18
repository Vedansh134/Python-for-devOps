# dictionary : Store data in key value pair

ec2_instance = {
    "name" : "web-server-test",
    "os" : "ubuntu",
    "ami" : "ami-hucw84jhhhhu2398389",
    "instance_type" : "t2.micro",
    "key" : "private",
    "network" : {
        "vpc" : "vpc_988fj4384848",
        "subnet" : "ap-south-1a",
        "sg-grp" : {
            "protocol" : "http",
            "port" : "80",
            "source" :  "sg-f909jjjjj",
            "destination" : "sg-t0895t905890j"
        }
    },
    "script" : {
        "install-server" : "f{Sudo} yum install nginx -y\n service nginx start\n service nginx enabled\n"
    }
}

# -------------------------------------------------------
# ---- use different dictionary methods

# access the value
name = ec2_instance.get("name")
print(f"Name of ec2 : {name}")

# access the keys
keys = ec2_instance.keys()
print(f"All keys : {keys}")

# access the nested keys
nested_keys = ec2_instance["network"].keys()
print(nested_keys)

# access the values
values = ec2_instance.values()
print(f"all values : {values}")

# access deeper nested value
nested = ec2_instance["network"]["sg-grp"]["protocol"]
print(f"Deeper nested value : {nested}")

# clear
ec2_instance.clear()
print(ec2_instance)

