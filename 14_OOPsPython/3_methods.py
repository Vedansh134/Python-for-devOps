# ------ Normal Methods (Instance Methods) :

# The "Worker" : These methods act on a specific object.
# The self Keyword : They always take self as the first argument.
# Use Case : Use this when the action depends on the specific data of that object (like starting a specific server).

# ------ Static Methods :
# The "Tool" : These are just regular functions that live inside a class for organization. They don't know anything about the object's data.
# The @staticmethod Decorator : They don't take self or cls.
# Use Case : Use this for "Utility" functions—things like validating an IP address format or converting units.

class CloudManager:
    def __init__(self, server, id):
        self.server_name = server
        self.instance_id = id

    # --- Normal method ---
    def start_server(self):
        print(f"Starting the {self.server_name} : {self.instance_id}")

    # --- Static method ---
    @staticmethod
    def elastic_ip(ip):
        print(f"Elastic IP : {ip}")

# --- How to use them ---

# 1. To use a Normal Method, you MUST create an object first

server = CloudManager("web_server", "amazon-805hf80")
server.start_server()
server.elastic_ip("34.54.5.4")
# print(CloudManager.start_server()) # gives error

# 2. To use a Static Method, you can call it directly from the Class
print(CloudManager.elastic_ip("192.168.1.1"))


# - Static methods (@staticmethod): Call directly via class (CloudManager.elastic_ip()).
# - Instance methods (normal methods): Need an object (server.start_server()).

# Why?- Static methods: No self, no instance data needed → call via class.
# - Instance methods: Need self (instance data) → need an object