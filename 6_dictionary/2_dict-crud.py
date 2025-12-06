# ===============================================================
# Perform CRUD operations in dictionary
# --- C : "create operation      - add a new key value pair"
# --- R : "Read operation        - get()/values()/keys()/items()"
# --- U : "update/edit operation - Update()"
# --- D : "delete operation      - pop()"
# ================================================================

aws_instance_info = {
    "name" : "webserver",
    "os" : "amazon-linux",
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
        "install-server" : "sudo yum install nginx -y\n service nginx start\n service nginx enabled\n"
    }
}

print('Perform different operations in dictionary')

# Create : Add a new key-value pair
aws_instance_info["ElasticIP"] = True
print("\nAfter create : ", aws_instance_info)

# Read : get()
print("\nRead operations")
get = aws_instance_info.get("vpc")
print("Value of vpc : ", get)

# Update : update()
aws_instance_info.update({ "ssh" : "22", "http" : "80"})
print("\nAfter updates : ", aws_instance_info)

# Delete : pop()
pop = aws_instance_info.pop("subnet")
print("\nPopped value : ", pop)
print("\nAfter delete : ", aws_instance_info)

