import sys

location = sys.argv[1].strip().lower()
type = sys.argv[2].strip().lower()

if location == "mumbai" or location == "hyderabad":
    if type == "t2.micro":
        print("It is used for normal workloads and charge ₹16.8/day")
    elif type == "t2.medium":
        print("high workload and charge ₹33.6/day")
    elif type == "t2.large":
        print("charge ₹67.2/day")
    else:
        print("you used other type and check docs")
else:
    print("Give me Indian(mumbai/hyderabad) location only")


