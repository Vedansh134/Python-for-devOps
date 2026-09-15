#
# ======================= Basic loop ============================
#

tech_list = ["aws","azure","linux","docker","k8s","ansible"]

for item in tech_list:
    print(f"Vedansh know : {item}")
    
    if len(item) >= 6:
        print("Name is normal")
        
    
# break statement
for i in range(1,100,2):
    print(f"No. : {i}")
    
    if i == 51:
        break
    

for j in range(5):
    print("printing")
    
    if j == 3:
        continue
    
    print(f"no. {j}")
    