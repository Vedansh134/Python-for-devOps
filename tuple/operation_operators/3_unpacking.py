# unpacking : Tuples can be unpacked into variables
# Syntax : var1, var2, var3 = tuple
# Note : The number of variables on the left side must match the number of elements in the tuple.

tuple1 = ("Frontend","Backend","Fullstack","DevOps")

# unpacking the tuple into variables
role1, role2, role3, role4 = tuple1

print(f"Role 1 : {role1}, \nRole 2 : {role2}, \nRole 3 : {role3}, \nRole 4 : {role4}")

# output :
# Role 1 : Frontend,
# Role 2 : Backend,
# Role 3 : Fullstack,
# Role 4 : DevOps
