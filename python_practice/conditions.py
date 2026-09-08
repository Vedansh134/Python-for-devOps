# 
# ======================== Condition in python =========================
#
# --- if condition 
# --- if-else condition
# --- if-elif-else condition
# --- nested conditions
# --- switch-case like
#
# =======================================================================
#

import time

# Deployment Settings
USER=input("\nEnter user role : ").lower().strip()
ENV=input("\nEnter your environment (prod/dev/qa/uat/others) : ").lower().strip()
DEPLOYMENT_BRANCH=input("\nEnter your deployment branch : ").lower().strip()


# System Metrics
# cpu_usage =72
# memory_usage = 65
# disk_usage = 88
# response_time = 2.3
# error_rate = 0.03 

backup=input("Take the backup before proceeding with the deployment.(yes/no) : ")


# =============================
# check branch
# =============================

# Define a list of allowed deployment branches
ALLOWED_BRANCHES = ["main","qa","uat"]

if DEPLOYMENT_BRANCH in ALLOWED_BRANCHES:
    print(f"✅ You can proceed with the '{DEPLOYMENT_BRANCH}' branch")
else:
    print(f"❌ Not proceed with {DEPLOYMENT_BRANCH} branch")
    exit()


# ======================
# Backup check
# ======================

if USER == "admin":
    
    if backup == "no":
        print("\n🚨 Backup not existing. Proceeding with backup first...")
        print("\tStart backup...")
        print("\tBackup take successfully ✅")
    else:
        print("📦 Backup exist, you can proceed with the deployment.")


# ==================================
# conditions for the deploy the app
# ==================================

if USER == "admin":
    print(f"\nUser is {USER},\nYou can start the deployment")
    
        
    if ENV == "prod":
        print("✅ Deploying to PRODUCTION - completed!")
        
        time.sleep(2)
        
        rate = int(input("Enter clear success rate in numeric : "))
        if rate >= 90:
            print("Wow, great passed reports!")
            time.sleep(2)
            
            scan_pass=True
            if scan_pass:
                print("App ready for production")
                time.sleep(5)
        
            
    elif ENV == "dev":
        print("✅ Deploying to DEV - No checks")
        
            
    elif ENV == "staging":
        print("✅ Deploying to STAGING - Basic checks only")
            
    else:
        print("❌ Invalid environemnt")
        
else:
    print(f"\nUser must be ADMIN not {USER}")
    exit()
    
print("Deployment is completed!")
