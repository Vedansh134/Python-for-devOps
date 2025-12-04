# Position Arguments
# Arguments passed during the function call must match the order of parameters defined in the function signature.

type = input("Enter your pet type : ")
name = input("Enter your pet name : ")

def describe_pet(animal_type,animal_name):
    result = f"I have {animal_type} and name is {animal_name}"
    return result

animal = describe_pet(type,name)
print(animal)

# Output :
# Enter your pet type : dog
# Enter your pet name : buddy
# I have dog and name is buddy
