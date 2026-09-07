# 
# ==================== Practice tuple ======================
# 
print("It is inmutable.\nCan hold multiple value.\nTuple is ordered, allowed duplicacy and unchangable")

# Defined a tuple
empty_tuple=()
print(type(empty_tuple))

tuple = (1,2,(4,5,"m"),"string",True)
print(f"Values of tuple : {tuple[::-1]}")
print(f"Print particular value : {tuple[1]}")
print(f"Print particular value : {tuple[2][1]}")
print(f"Print inner octet value in reverse : {tuple[2][::-1]}")

# =======================================================================================================
# Different operations in tuple

# Concatenation 
tup1 = ("frontend","backend")
tup2 = ("devops","aipos","mlops")

concat = tup1 + tup2 
print(f"Concatenation of tuple : {concat}")


# Repeat 
print(f"Multiple times print tuple : {tup2*3}")


# Unpacking tuple into values
role1, role2, role3 = tup2
print(f"\nCurrent opennings : \nPosition 1 : {role1}\nPosition 2 : {role2}\nPosition 3 : {role3}")


# Slicing in tuple
slicing1 = tup2[1:3]
print(f"Slicing : {slicing1}")


# =======================================================================================================
# Different operators in tuple


# in operation : To check element is present or not in tuple
devops=("aws","docker","k8s","jenkins","ansible")
find="azure"

if find in devops:
    print(f"{find} is present in devOps tools list")
else:
    print(f"{find} is'nt present in devOps tools list")


# not-in operaation
if find not in devops:
    print("yes it is not present in list")
else:
    print('It is present in list')