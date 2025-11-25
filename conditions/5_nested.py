# nested statements in python are conditional statements that contain one or more conditional statements inside them.

is_citizen = input("Are you a Indian Citizen : (Yes/No) ? ")
age = int(input("Enter your age : "))

if is_citizen == "India":
    print("You know about india...")
    if age >= 18:
        print("You are eligble for vote")
    else:
        print("You are not eligble for vote")
else:
    print("You are not a Indian citizen")

print("This always run")
