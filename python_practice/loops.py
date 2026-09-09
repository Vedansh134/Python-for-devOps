#
# ========================== loops in python ===========================
#
# for loop
# range in loop

import time
import random
from datetime import datetime

def devops_monitoring_system():
    infrastructure = {
        "datacenter": {
            "server-1": {"cpu": 45, "memory": 60, "status": "running", "region": "us-east-1a"},
            "server-2": {"cpu": 78, "memory": 85, "status": "running", "region": "us-east-1b"},
            "server-3": {"cpu": 92, "memory": 88, "status": "warning", "region": "us-west-1c"},
        },
        "containers": {
            "frontend" : {
                "cpu" : 45,
                "mem" : 78,
                "status" : "running"
            },
            "backend" : {
                "cpu" : 34,
                "mem" : 89,
                "status" : "warning"
            },
            "database" : {
                "cpu" : 97,
                "mem" : 91,
                "status" : "critical"
            }
        }
    }
    
    # only access above dictionary
    print(f"Particular server cpu consumption : {infrastructure["datacenter"]["server-1"]["cpu"]}")
    
    
    
# call a function
devops_monitoring_system()