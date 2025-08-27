# Inside list contain dictionary
# list of dictionary
# dictionary used for complicated structure/record
# like emp.details, stu details etc

inst_info = [
    {
        "id" : "instance-001",
        "type" : "t2.micro",
        "ami" : "ami-12345678",
        "security-grp" : [22, 443]
    },
    {
        "id" : "instance-002",
        "type" : "t2.small",
        "ami" : "ami-87654321",
        "security-grp" : [20,21]
    },
    {
        "id" : "instance-003",
        "type" : "t2.medium",
        "ami" : "ami-13579246",
        "security-grp" : [25, 465]
    }
]

# Acess the above dictionary
print(inst_info[1]["type"])

# change the value
inst_info[2]["type"] = "t3.large"
print(inst_info[2]["type"])

# Iterating Through Keys and Values using nested loops
for instance in inst_info:
    for key, value in instance.items():
        print(f"keys : {key} and values : {value}")
