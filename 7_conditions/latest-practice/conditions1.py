# Conditions allow you to make decisions in your code. They execute different blocks of code based on whether a condition is True or False.

state = input("Enter ec2 state : ")
state = state.capitalize().strip()

if state == "Stop":
    print(f"Instance is stopped : {state}")
elif state == "Running":
    print(f"Instance is running : {state}")
elif state == "Terminate":
    print(f"Instance is trminated : {state}")
else:
    print(f"Please give me right keyword : {state}")