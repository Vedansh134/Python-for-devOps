# Class (The Blueprint) :

# It is a logical template.
# It doesn't "exist" in the real world
# It defines what properties (attributes) and actions (methods) the resource will have.

# Object (The Instance) :

# It is the physical reality.
# It is created from the class.
# It takes up memory.
# You can create 100 objects from just 1 class.


# ----- defined class (The Blueprint) -----
class S3Bucket:
    def __init__(self, bucket_name, region, encryption=True):
        # Attributes
        self.bucket_name = bucket_name
        self.region = region
        self.encryption = encryption
        self.files = []

    # method (action)
    def upload_files(self, file_name):
        self.files.append(file_name)
        print(f"{file_name} uploaded successfully to {self.bucket_name}")

# ----- objects (actual objects) -----
object_bucket = S3Bucket("web_server_123f", "ap-south-1")
backup_bucket = S3Bucket("db_backups_34fg", "ap-south-2")

print(object_bucket.encryption)

# ----- Using the objects ------
object_bucket.upload_files("ubuntu-img")
backup_bucket.upload_files("sql_dump_jan1.zip")