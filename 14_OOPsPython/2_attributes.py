# Attributes
# 2 types of attributes

# ==== Class Attributes : Own by class and common for all objects. Shared all objects (Instances) of a class.

# Example :-
# Every AWS resource belongs to a "Region" (like ap-south-1). If the whole company only uses one region, that region is a Class Attribute.

# -----------------------------------------------

# ==== Object Attributes : Instance attributes diff for diff object. Uniques to specfic object.

# Example :-
# Every EC2 server has its own "Name" and "Instance ID


class EC2Instance:
    # define class attributes
    provider = "AWS"
    region = "ap-south-1"

    def __init__(self, name, instance_type):
        # define instance(object) attributes
        self.server = name
        self.instance_type = instance_type
        self.status = "Stopped"

    def start_server(self):
        self.status = "Start"
        print(f"{self.server} is now {self.status} on {self.provider}!")

# --- creating objects ---

web_server = EC2Instance("web-app-env","t2-micro")
prod_server = EC2Instance("web-app-prod","t3.medium")

# Accessing attributes
print(web_server.server) # web-app-env unique
print(prod_server.server) # web-app-prod unique

# Same -- AWS
print(web_server.provider)
print(prod_server.provider)

# Both -- web-app-prod is now Start on AWS!
print(prod_server.start_server())
print(web_server.start_server())