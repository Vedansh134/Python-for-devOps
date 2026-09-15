#
# ========================== loops in python ===========================
#
# for loop
# range in loop
#

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
            "frontend" : {"cpu" : 45, "memory" : 78, "status" : "running"},
            "backend" : {"cpu" : 34, "memory" : 89, "status" : "warning"},
            "database" : {"cpu" : 97, "memory" : 91, "status" : "critical"}
        }
    }
    
    # ===================================
    # == Define threshold parameters
    # ===================================
    
    thresholds = {
        "cpu_warning"   : 90,
        "cpu_critical"  : 95,
        "mem_warning"   : 85,
        "mem_critical"  : 90,
    }
    
    total_issues = 0
    critical_issues = 0
    
    print("------------ Health check report -------------")
    
    # only access above dictionary
    print(f"Particular server cpu consumption : {infrastructure["datacenter"]["server-1"]["cpu"]}")
    
    for category, services in infrastructure.items():
        #print(f"\nServer Category : {category.upper()}")
        
        for deploy_type, metrics in services.items():
            #print(f"Deployment type : {deploy_type}")
            
            # Get status
            status = metrics.get("status","unknown")        
            memory = metrics.get("memory",0)
            cpu = metrics.get("cpu",0)
            
            
            # Determine health status using conditions
            health_icon = "✅"
            health_status = "Healthy"
            
            if status == "critical" or cpu >= thresholds["cpu_critical"] or memory >= thresholds["mem_critical"]:
                health_icon = "🚨"
                health_status = "Critical"
                total_issues += 1
                critical_issues += 1
                
            elif status == "warning" or cpu >= thresholds["cpu_warning"] or memory >= thresholds["mem_warning"]:                      
                health_icon = "⚠️"
                health_status = "Warning"
                total_issues += 1
                
            else:
                print(f"Status : {health_status} {health_icon} | CPU : {cpu}% | MEM : {memory}%")
            
    
    # Summary for the issues
    print("------ Server issue summary -------")
    print(f"Total Issues    : {total_issues}")
    print(f"Critical Issues : {critical_issues}")
    
    if total_issues > 0 :
        print("🚨 Action: Page on-call engineer immediately!")
    elif critical_issues > 0:
        print("⚠️  Action: Create Jira ticket, monitor closely")
    else:
        print("✅ All system works fine!")
    
    
# call a function
devops_monitoring_system()