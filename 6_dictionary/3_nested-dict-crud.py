# ===============================================================
# Perform CRUD operations in nested dictionary
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

# =========================
# Nested operations

# Create : Add a new key-value pair
aws_instance_info["ebs"]["IOPS"] = "2500"
print("\nAfter update : ", aws_instance_info["ebs"])

# Read : get()
print_nested_ele = aws_instance_info["tags"]["server"]
# === or print_nested_ele = aws_instance_info.get("tags").get("server")
print(print_nested_ele) # test

# Update : update()
docker_install = {"docker-install" : "\n sudo yum install docker -y\n svc docker enabled\n svc docker start"}
aws_instance_info["script"].update(docker_install)

# Delete : pop()
pop = aws_instance_info["tags"].pop("server")
print(pop)

# now print dictionary after delete
print("\n")
print(aws_instance_info) # subnet and tags[0] not found

